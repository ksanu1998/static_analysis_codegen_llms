# NLP_Group37
### Target 1.2.1
Pipeline is split into 3 stages:<br>
* Input processing - Process `XLCost` C++ code to the desired format (function signature, docstring, and first function call)
* LM - Make a forward pass through the LM (`code llama 7b`) to generate / complete code, evaluate the LM using the generated / completed code agains the original (unmasked) input
* Static Analysis - Check for static errors in the generated code using `cppcheck`, and generate report
