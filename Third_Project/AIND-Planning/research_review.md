## Udacity - Artificial Intelligence Nanodegree
## Research Review by Tomasz Szyborski

## Historical Developments in the field of AI Planning and Search

# STRIPS and ADL

In early 1970s Richard E. Fikes and Nils J. Nilsson created a program what can be called first AI - 
in order to “find a sequence of operators in a space of world models to transform a given
initial world into a model in which a given goal formula can be proven to be true”[1] for planning component of the software for the Shakey robot project[2].
STRIPS was the first major planning system. The most influential element of STRIPS was its
representation language as it is cobble stone for expressing automated planning problems.
After almost 20 years - in 1987 - Action Description Language (ADL) was introduced to overcome weaknesses of STRIPS - such as postitive-only literals in states or conjunctions-only goals.

# PDDL (P​lanning D​omain D​efinition L​anguage)
It was first developed by Drew McDermott and his colleagues in 1998 (inspired by STRIPS and ADL among others) mainly to make the 1998/2000 International Planning Competition (IPC) possible[1].
PDDL has become the standard planning domain and problem description
language for the International Planning Competition since its launch. "The adoption of a common formalism for describing planning domains fosters far greater reuse of research and allows more direct comparison of systems and approaches, and therefore supports faster progress in the field. A common formalism is a compromise between expressive power (in which development is strongly driven by potential applications) and the progress of basic research (which encourages development from well-understood foundations). The role of a common formalism as a communication medium for exchange demands that it is provided with a clear semantics."[3]
PDDL was created to express the “physics” of a domain - presence of predicates, possibilities of the actions, structure and effects of the actions[4].
The domain definition contains the domain predicates, operators or actions.
The problem definition contains the objects present in the problem, the initial state description and the goal. 

# Situation Calculus
Introduced by John McCarthy in 1963 - Situation calculus represents changing scenarios as
a set of first-order logic formula and its components are situations - history of actions, fluents - truth values of given situations and actions - forming the domain[5].
Situation calculus is used for planning by asking for a situation in which a goal is true which is led to by using answer extraction. The situation can be interpreted as a sequence of actions for the agent to perform.



References
1. Richard E. Fikes, Nils J. Nilsson (Winter 1971). "STRIPS: A New Approach to the Application of Theorem
Proving to Problem Solving" (PDF). Artificial Intelligence. 2​ (3–4): 189–208.
2. Russell, Stuart J.; Norvig, Peter (2003), Artificial Intelligence: A Modern Approach (2nd ed.), Upper Saddle
River, New Jersey: Prentice Hall, ISBN 0-13-790395-2
artificial-intelligence-planning-with-strips-a-gentle-introduction/
3. Fox, M.; Long, D. (2002). "PDDL+: Modeling continuous time dependent effects". Proceedings of the 3rd International NASA Workshop on Planning and Scheduling for Space. CiteSeerX 10.1.1.15.5965
4. McDermott, Drew; Ghallab, Malik; Howe, Adele; Knoblock, Craig; Ram, Ashwin; Veloso, Manuela;
Weld, Daniel; Wilkins, David (1998). "PDDL---The Planning Domain Definition Language" (PDF).
Technical Report CVC TR98003/DCS TR1165. New Haven, CT: Yale Center for Computational Vision
and Control. CiteSeerX 10.1.1.51.9941 .
5. J. McCarthy and P. Hayes (1969). Some philosophical problems from the standpoint of
artificial intelligence. In B. Meltzer and D. Michie, editors, Machine Intelligence, 4:463–502.
Edinburgh University Press, 1969.