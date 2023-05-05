# TFLearn Text Generation

<h2>How to run (Bash):</h2>
<ol type="1">
    <li>
        <strong>Add Dependencys:</strong><br>
        Add required dependencies before running Tensorflow training (pip3 modules): <br>
        <em>./addDependency.sh</em><br>
    </li><br>
    <li>
        <h3><strong>Train Model:</strong></h3><br>
        Will train the model. if one is not present, it will also create one. It will run a default of one epoch, but can be changed through the bash command (see examples below). <br>
        
        <em>./trainModel.sh</em><br>
    </li><br>
    <li>
        <h3><strong>Generate Text:</strong><br></h3>
        <em>./generate.sh [base_text] [n_char = 25] </em><br>
        Example: <em>./generate.sh hello 25 </em><br>
        Example: <em>./generate.sh world 15 </em><br>
    </li><br>
</ol>
