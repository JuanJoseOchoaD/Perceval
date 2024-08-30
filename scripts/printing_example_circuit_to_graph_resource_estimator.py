# MIT License
#
# Copyright (c) 2022 Quandela
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# As a special exception, the copyright holders of exqalibur library give you
# permission to combine exqalibur with code included in the standard release of
# Perceval under the MIT license (or modified versions of such code). You may
# copy and distribute such a combined system following the terms of the MIT
# license for both exqalibur and Perceval. This exception for the usage of
# exqalibur is limited to the python bindings used by Perceval.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from perceval.converters import CircuitToGraphConverter
from perceval.converters import ResourcesEstimator
from qiskit.circuit.random import random_circuit
from perceval import pdisplay
import networkx as nx
import perceval as pcvl
qiskit_circuit = random_circuit(8, 10, max_operands=2)  # Generate a random circuit for demonstration
converter = CircuitToGraphConverter(qiskit_circuit=qiskit_circuit)

# Generate the graph
graph = converter.generate_graph()

# Plot the graph
pdisplay(graph, output_format=pcvl.Format.MPLOT)

print('Single calculation       ', converter.graph_k_clustering_and_cnots_needed()[0])
print('Third single calculation ', converter.graph_k_clustering_and_cnots_needed()[0])
print('Second single calculation', converter.graph_k_clustering_and_cnots_needed()[0])

print('CX:', converter.graph_k_clustering_and_cnots_needed()[1])
print('Choosing min  cnot', converter.graph_k_clustering_and_cnots_needed(compute_with_min_cnots=True)[0])
print('CX:', converter.graph_k_clustering_and_cnots_needed(compute_with_min_cnots=True)[1])

estimator = ResourcesEstimator(qiskit_circuit)
print("Optimal Encoding:", estimator.encoding)
print("Number of Physical 2-Qubit Gates:", estimator.num_entangling_gates_needed)
print("Number of needed modes for this encoding:", estimator.num_modes_needed)
print("Number of photons needed for this encoding:", estimator.num_photons_needed)

custom_encoding = [[0, 1], [2, 3], [4], [5], [6, 7]]

estimator_with_encoding = ResourcesEstimator(qiskit_circuit, custom_encoding)
print("Custom Encoding:", estimator_with_encoding.encoding)
print("Number of Physical 2-Qubit Gates:", estimator_with_encoding.num_entangling_gates_needed)
print("Number of needed modes for this encoding:", estimator_with_encoding.num_modes_needed)
print("Number of photons needed for this encoding:", estimator_with_encoding.num_photons_needed)




pdisplay(nx.complete_graph(5), output_format=pcvl.Format.MPLOT)
