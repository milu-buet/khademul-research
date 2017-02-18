# data conversion

# 3 : 402.1 ;  5 : 25.66 ;  6 : 28.2 ;  7 : 12.44 ;  8 : 16.64 ; 
from __future__ import print_function

input_file = 'Philadelphia_trips.txt'
out_file = 'out.txt'
mat_out_file = 'mat_out.txt'
dimension = None

def read_dim(first_line):
	dimension = int(first_line.split(">")[1].strip())
	print("Dimension discovered: %s"% (dimension,))

	return dimension

def data_reader(str,id):

	if len(str) <= 1:
	 return None
	all_data = str.split(";")
	for a_data in all_data:

		paired_data = a_data.strip().split(":")
		des = paired_data[0].strip()
		flow = paired_data[1].strip()

		return id,des,flow
output_file = open(out_file, 'w')
mat_output_file = open(mat_out_file, 'w')

def prepare_matrix(dim):
	 demand_matrix = {}
	 for i in range(1,dim+1):
	 	for j in range(1,dim+1):
	 		demand_matrix[i,j] = 0

	 return demand_matrix

def show_demand_matrix(demand_matrix,dim):

	 for i in range(1,dim+1):
	 	for j in range(1,dim+1):
	 		out_matrix_line = "%s "%(demand_matrix[i,j],)
	 		#print(out_matrix_line,end="")
	 		mat_output_file.write(out_matrix_line)
	 		#print(out_matrix_line)

	 	mat_output_file.write("\n")
	 	#print("\n")

demand_matrix = None
with open(input_file) as f:
    lines = f.readlines()
    #print lines
    reader_id = 0
    read_start = False
    dimension = read_dim(lines[0])
   
    demand_matrix = prepare_matrix(dimension)


    print("started....")
    print("list creation in process....")
    for line in lines:
    	title_line = line.find("Origin")

    	if title_line == 0:
    		reader_id+=1
    		read_start = True
    		#print line
    	elif read_start:
    		new_data =  data_reader(line,reader_id)
    		if new_data:
    			id,des,flow = new_data
    			#print(int(des))
    			demand_matrix[reader_id,int(des)] = flow
    			#print(new_data)
    			output_file.write("%s %s %s\n"% (id,des,flow))
    print("list creation ended....")

print("demand matrix creation in process....")
show_demand_matrix(demand_matrix,dimension)
print("demand matrix creation done....")

print("ended....")


