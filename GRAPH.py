#!/usr/bin/env python
# coding: utf-8

from pprint import pprint


class Graph:
    # Adjacency list
    def adjacency_list(self):
        graph = dict()
        graph['A'] = ['B']
        graph['B'] = ['C', 'F', 'G', 'D']
        graph['C'] = ['D', 'E', 'F']
        graph['D'] = ['G', 'H', 'J']
        graph['E'] = ['D']
        graph['F'] = ['J']
        graph['G'] = ['H']
        graph['H'] = ['I']
        graph['I'] = []
        graph['J'] = ['H']

        for key in graph:
            graph[key] = sorted(graph[key])
        return graph

    def get_adjacency_list(self, graph):
        print('=== adjacency list ===')
        tmp = []
        for item in graph.items():
            print(item[0] + ' --> ' + str(item[1]))

    def adjacency_matrix(self, graph):
        # adjacency_matrix
        matrix_elements = sorted(graph.keys())
        cols = rows = len(matrix_elements)
        adjacency__matrix = [[0 for x in range(rows)] for y in range(cols)]
        edges_list = []

        print('=== adjacency matrix ===')
        for key in matrix_elements:
            for titik in graph[key]:
                edges_list.append((key, titik))

        print('  A  B  C  D  E  F  G  H  I  J')
        for edge in edges_list:
            index_pertama_vertex = matrix_elements.index(edge[0])
            index_kedua_vertex = matrix_elements.index(edge[1])
            adjacency__matrix[index_pertama_vertex][index_kedua_vertex] = 1
        pprint(adjacency__matrix)


def main():
    graph = Graph()
    gr = graph.adjacency_list()
    graph.get_adjacency_list(gr)
    graph.adjacency_matrix(gr)


if __name__ == '__main__':
    main()
