number_of_students = int(input("How many students on the course? "))
size_group = int(input("Desired group size? "))


number_of_groups_formed = (number_of_students / size_group) if number_of_students % size_group == 0 else (number_of_students / size_group) + 1

print(f"Number of groups formed: {number_of_groups_formed}")