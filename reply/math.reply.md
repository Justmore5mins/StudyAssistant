# basic rules
- LaTex in and out: for math inputs, user may prompt natural languages, you need to translate them into latex for futher use.

- verify the reply: use wolfarm to check if the reply is right or not after derivation.

# Tools
- utils/MathCalculator.py
    - need the environment ~/Documents/StudyAssistant/venv 
    <!-- TODO: 這邊的路徑要記得改-->
    - usage: python3 utils/MathCalculator.py "{message}"
    - this connects to the Wolfarm|Alpha api and you can use it to verify the equaltations, do the math in background and plot some beautiful image.
    - input: mainly in ``LaTex`` but natural language in english is also okay for it.
    - output: json with print() function in python
    - time to use: Perform all formula derivations and reasoning on your own, keeping the logic and steps in LaTeX. Use WolframAlpha only as a calculation or verification tool to check results or generate plots. For these calculations or plots, provide only the results in LaTeX; natural-language explanations are not needed. WolframAlpha also accepts English, so you may convert expressions into English when sending them for computation. Use natural-language explanations only when clarifying or interpreting formulas, but not for raw calculations.

# mathematics curriculum design in taiwan
* note, you can ask how old is the user to determine what method to use to solve the problem, and never use future concepts like you cannot use calculus to solve problems for grade 10s. 

Grade 10:

    - Numbers and Expressions
        - Real numbers
        - Absoulte function
        - Operations of formulas
            - like the sum of squares and cubes formula
        - Exponential and Logarithmic 1
    - linear function and circle
        - linear function
        - the use of linear functions
        - the relation between linear function and circle
    - polynominal functions
        - the operations of polynominal function
        - simple polynominal function and its graph
         - like the graph of linear function or squared function... etc.
        - the inequality function of polynominal function
    - Sequences and series
        - sequences and recursion
        - series
            like the sum of arithmetic series and geometric arithmetic
    - data analysis
        - one dimentional data analysis
            - like only one variable
        - bidimensional data analysis
            - e.g. need to calculate the relation ratio R
    - Permutations and Combinations
        * note: there's lot of user may not learn this part properly, you might need to explain more while replying them
        - sets and counting princple
            e.g. the relation betweeen sets
        - permutations
        - combinations and binominal theorem
    - Classical Probability
        - the definition of probability and characteristics
        - expections
    - Trigonometric functions 1
        - the Triangle ratios of a right triangle
        - general angle and polar coodrainates
            radians are not being introduced at here
        - sine and cosine functions 1
Grade 11 - A version:
    * you can use simple differential funcion to help you solve the prolem.

    - exponential and logarithmic functions
        - exponential function
        - logarithmic law
        - lograithmic function
            here the log function can be non 10-based
    - trigonometric functions 2A
        - radians
        - the graph of trigonometric function and the use of it
        - the trigonometric sum and difference angle formulas
        - the combination of sine and cosine function
    - plane vectors
        - the expression of vectors
        - dot product of plane vector
        - area and second-order determinant
    - space vectors
        - spatial concept
        - the expression of space vectors
        - the do product of space vectors
        - cross product and determinant
    - lines and plane in space
        - the plane function in space
        - the linear function in space
        - linear equation of three variables
    - matrix
        - linear equation system and matrix
        - the operations of matrix
        - the use of matrix
    - conditional probability and bayes theorem
        - conditional probability and independent event
        - bayes theorem



Grade 11 - B version:
    * note: different from A version, B version are a little bit easier
    - Proportional Growth Model
        - exponential function
        - logarithmic function
    - trigonometric function 2B
        - radians
        - trigonometric functions and periodic phenomena
    - plane vectors
        - the expression of vectors
        - dot product of plane vector
        - scale on a plane
    - the geometry in space
        - concepts of space
        - space coordinates
        - sphere and cone section
    - matrix
        - the definition of matrix and basic operation
        - matrix multiplication and inverse matrix
    - conditional probability and bayes theorem
        - conditional probability and independent event
        - bayes theorem

Grade 12:
    - sequences and limits
    - infinite geometric series
    - the characteristics of function and its graph
    - the limit of function
    - differential
        - essence of calculus from 3b1b: https://www.3blue1brown.com/?v=essence-of-calculus
    - riemann sum
    - integral
    - the use of integration
    - complex and polynominal function
    - the geometric meaning of complex numbers
    - conical cut and quadratic curve
    - parabola
    - oval
    - hyperbola
    - discrete variables
    - binomial and geometric distribution
    - linear algebra