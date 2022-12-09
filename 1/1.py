import os



if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__),"input")
    with open(input_path,'r') as input_f:
        data = [sum([int(j) for j in raw.split('\n') if j != '']) for raw in input_f.read().split('\n\n')]
        numbered_data = list(zip(range(1,len(data)+1),data))
        numbered_data.sort(key=lambda x: x[1],reverse=True)
        #print(numbered_data)
        print(f"Answer #1:\n\tElf position: {numbered_data[0][0]}\n\t Calories carried: {numbered_data[0][1]}")
        print(f"Answer #2:\n\tTop three elves total calories: {numbered_data[0][1] + numbered_data[1][1] + numbered_data[2][1]}")

        input_f.close()