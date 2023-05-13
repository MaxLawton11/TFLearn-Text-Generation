# TFLearn Text Generation

<hr>
<h1>Execution (Bash):</h1>
<ol type="1">
    <li>
        <h2><strong>Add Dependencys:</strong></h2>
        Add required dependencies before running Tensorflow training. This will add the required pip3 modules. If pip is unavailable, install the following from your preferred method: numpy, pillow, tflearn, tensorflow. <br>
        <h4><strong>Command: </strong></h4>
        <em>./addDependency.sh</em><br>
    </li>
    <li>
        <h2><strong>Train Model:</strong></h2>
        Will train the model. if one is not present, it will also create one. It will run a default of one epoch, but can be changed through the bash command (see examples below). <br>
        <h4><strong>Command: </strong></h4>
        <em>./trainModel.sh [n_epoch = 1] <em><br>
        Example: <em>./trainModel.sh </em><br>
        Example: <em>./trainModel.sh 5 </em><br>
    </li>   
    <li>
        <h2><strong>Generate Text:</strong><br></h2>
        (Note: Must only pass one word for base_text. If words are separated by a space, you will get errors due to overlaping argvs.) 
        <h4><strong>Command: </strong></h4>
        <em>./generate.sh [base_text] [n_char = 25] </em><br>
        Example: <em>./generate.sh hello </em><br>
        Example: <em>./generate.sh world 15 </em><br>
    </li><br>
</ol>
