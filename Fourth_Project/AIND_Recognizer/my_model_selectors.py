import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on BIC scores
        # raise NotImplementedError
        lowest_bic = np.float('inf')
        best_model = None

        for n_components in range(self.min_n_components,
                                  self.max_n_components + 1):
            try:
                model = self.base_model(n_components)

                # BIC = −2 log L + p log N
                # L = log likelihood
                # p = number of parameters in model
                # N = number of data points

                log_L = model.score(self.X, self.lengths)

                # p = n^2 + 2*d*n - 1
                # n = components
                # d = features
                p = (n_components ** 2
                    + 2 * model.n_features * n_components 
                    - 1)

                # BIC = −2 log L + p log N
                bic = -2 * log_L + p * np.log(len(self.X))

                if bic < lowest_bic:
                    lowest_bic = bic
                    best_model = model
            except Exception:
                pass

        return best_model

class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on DIC scores
        # raise NotImplementedError
        highest_dic = np.float('-inf')
        best_model = None
        for n_components in range(self.min_n_components,
                                  self.max_n_components + 1):
            try:
                # train the whole model with this number of components
                model = self.base_model(n_components)
                # get the data for the word we are trying to score for
                X_word, lengths_word = self.hwords[self.this_word]
                # log likelihood of total model on all data with n_components
                # of predicting the target word
                target_log_L = model.score(X_word, lengths_word)
            except Exception:
                pass

            anti_Log_L = 0
            word_count = 0
            for word in self.words:
                if word is not self.this_word:
                    # get the data for each other word
                    X_word, lengths_word = self.hwords[word]
                    try:
                        # score the log likelihood of the model misguessing
                        # this word instead
                        log_L_word = model.score(X_word, lengths_word)
                        anti_Log_L += log_L_word
                        word_count += 1

                    except Exception:
                        continue

            # DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
            # DIC = log likelihood - average log likelihood of other words
            dic = target_log_L - (1 / (word_count - 1)) * anti_Log_L

            if dic > highest_dic:
                highest_dic = dic
                best_model = model

        return best_model


class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def run_model(self, n_components, X_train, lengths_train, X_test,
                  lengths_test):
        model = GaussianHMM(n_components=n_components, covariance_type="diag",
                            n_iter=1000, random_state=self.random_state,
                            verbose=False).fit(X_train, lengths_train)
        log_L = model.score(X_test, lengths_test)
        return log_L

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # raise NotImplementedError
        
        best_model = None
        highest_average = np.float('-inf')
        n_splits = min(len(self.sequences), 3)

        for n_components in range(self.min_n_components,
                                  self.max_n_components + 1):
            total_log_L = 0
            iterations = 0
            try:
                if n_splits > 1:
                    split_method = KFold(n_splits=n_splits)
                    seq_splits = split_method.split(self.sequences)
                    for cv_train_idx, cv_test_idx in seq_splits:
                        X_train, lengths_train = combine_sequences(
                            cv_train_idx, self.sequences)
                        X_test, lengths_test = combine_sequences(
                            cv_test_idx, self.sequences)

                        log_L = self.run_model(n_components, X_train,
                                              lengths_train, X_test,
                                              lengths_test)

                        total_log_L += log_L
                        iterations += 1
                else:
                    log_L = self.run_model(n_components, self.X, self.lengths,
                                          self.X, self.lengths)
                    total_log_L += log_L
                    iterations += 1

                average_log_L = total_log_L / iterations
                if average_log_L > highest_average:
                    highest_average = average_log_L
                    best_model = self.base_model(n_components)

            except Exception:
                pass

        return best_model
