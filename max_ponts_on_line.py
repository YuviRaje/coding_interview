'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

coords = [(1,2), (4,5)]

def max_points_on_same_line(coords):
	result = 0

	for i in range(len(coords)):
		slope_map = map()

		for j in range(i+1, len(coords))
			y_slope = coords[j][1] - coords[i][1]
			x_slope = coords[j][0] - coords[i][0]
			
			if x_slope != 0:
				slope = (y_slope * 1.0 ) / x_slope
			else:
				slope = 'inf'

			slope_map[slope] += 1

		for each in slope_map:
			max_lines = max(max_lines, slope_map[each])

		result = max(result, max_lines)

	return result

