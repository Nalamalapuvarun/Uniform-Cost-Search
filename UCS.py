import sys
import heapq


f = open(file_name)
for line in f:
    if ("END OF INPUT" in line):
        break
    a, b, cost=line.split()
    graph={}
    graph.setdefault(a, []).append((b, cost))
    graph.setdefault(b, []).append((a, cost))

f.close()
def main(file_name, source, destination):
	# call the UCS function
	result = UCS(G,Source,Destination)

	print "\n\nFinal output: \n"
	# print the result in the required format
	if result == None:
		print "\ndistance: infinity\nroute:\nnone\n"
	else:
		print "\ndistance:",result[0],"km\nroute:"
		for line in result[1]:
			print "%s to %s, %s km" % (line[1],line[0],line[2])
		print ""

	pass
def UCS(graph, s, goal):
	# define dummy variables for use
	nodesQ = []
	visited_nodes = {}
	prev_nodes = {}

	# using heap for mainitng a queue
	heappush(nodesQ,(0,s,None,0))
	for nodes in graph:
		visited_nodes[nodes] = False
		prev_nodes[nodes] = None
	i = 1
	# mark all visited and previous nodes False and None
	while len(nodesQ) != 0:
		# pop the least cost node from heap and analyse it
		print "\nFringe at Loop#: ",i
		print nodesQ
		i = i+1
		total_cost, current_node, prev_node, link_cost = heappop(nodesQ)
		if visited_nodes[current_node] == False:
			visited_nodes[current_node] = True
			prev_nodes[current_node] = []
			prev_nodes[current_node].append(prev_node)
			prev_nodes[current_node].append(link_cost)
			# if goal return the total route
			if current_node == goal:
				final = []
				while current_node != s:
					temp = []
					temp.append(current_node)
					for i in prev_nodes[current_node]:
						temp.append(i)
					final.append(temp)
					current_node = prev_nodes[current_node][0]
				final.reverse()
				# retrn total cost and final path
				return total_cost,final
			# else explore neighbours
			for neighbors, ncost in graph[current_node].items():
				if visited_nodes[neighbors] == False:
					this_link_cost = ncost
					new_cost = total_cost + ncost
					heappush(nodesQ, (new_cost, neighbors, current_node, ncost))
	# return none if no path found

	return None
	pass
