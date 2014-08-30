def gready_algorithm(job_weight_lenght, case_1, bound):
    job_weight_lenght.sort(key = bound)
    job_weight_lenght.sort(key = case_1)

    time = 0
    result = 0
    for i in range(len(job_weight_lenght)):
        time += job_weight_lenght[i][1]
        result += time*job_weight_lenght[i][0]
    return result

def read_file():
    job_weight_lenght = []

    for line in open("task1.txt","r").read().split("\n"):
        a, b = [int(x) for x in line.split()]
        job_weight_lenght.append((a,b))
        #job_length.append(a[1])
    case_1 = lambda(a, b): -(a-b)
    case_2 = lambda(a, b): -float(a)/b
    bound = lambda(a, b): -a
    return job_weight_lenght, case_1, bound, case_2

def main():
    j, c1, b, c2 = read_file()
	#task1
    print(gready_algorithm(j, c1, b))
    print(gready_algorithm(j, c2, b))

main()
