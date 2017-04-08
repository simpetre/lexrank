# **Lexrank**
Lexrank is an article summarisation methodology implemented by [https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume22/erkan04a-html/erkan04a.html](Erkan and Radev). It applies the PageRank algorithm to the problem of text summarisation - at its heart, breaking up the document to be summarised into its constituent sentences and then transforming the sentences into a graph, where edges of the graph represent sentences and vertices join sentences with high similarity. PageRank is then run over the graph, and the sentences with the highest "prestige" are returned as the most important ones in the document (and thus used to summarise the document most accurately), in much the same way as PageRank returns webpages with higher prestige.
