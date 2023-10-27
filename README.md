# NLP_Group37
### Target 1.2.1
Pipeline is split into 3 stages:<br>
* Input processing - Process `XLCost` C++ code to the desired format
* LM - Forward pass through the LM to generate code, and evaluate model using the generated code
* Static Analysis - Check for static errors in the generated code using `cppcheck`
