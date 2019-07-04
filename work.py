from collections import Iterator,Ierable
list = [1,2,3]
isinstance(list,Iterable)
gene = (x*x for x in [1,2,3,])
isinstance(gene,Iterable)
listIter = iter(list)
isinstance(listIter,Iterator)
