# SNACS project

This project supposes that you have already installed boot in a folder in the same directory as the main folder of the project with name boost_1_77_0.

1. How to run the code

 i). install c++ library 'boost'
 ii). compile the file using command 'make'
 iii). run the program using command in the format as:

    './motif Type_of_motif_pattern Number_of_layers Number_of_nodes Network_name Threshold'
    example: ./motif 2 10 200 test.txt 0.6 1 output.txt
    
    Each parameters is explained as follows:
    a.Type of motif pattern: 1 (Feedforward); 2 (Bifan); 3 (Biparallel); 4 (Cascade)
      We currently only support 4 basic motif patterns. To support large motif pattern, you can refer to paper https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5053092/. 

    b. Number of layers: integer
    c. Number of nodes: integer
    d. Network name: path to the network file
    e. Threshold (The embeddings are appearing in at least how many layers of network, percentage number): float number (0, 1]
    f. Frequency measure: 1 (F1); 2 (F2); 3 (F3)
    g. Output name: path to the output file


2. Input network format
Each row is an edge: source_node tab target node
We use '-----' as a line to seperate each layer; and also add '----' at the end of file to indicate this layer of network is finished.

See test.txt file as an example.

3. output of program
   
   Given a motif type, we output 1) the number of motifs we have found, 2) the running time, 3) the layers which have these motifs, 4) a file save the edges of all these motifs (If the motif pattern has n edges, then every n edges constitue a motif embedding.
