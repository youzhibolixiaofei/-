def describe_pet(animal_type, pet_name='pangpang'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='wangwang')
describe_pet('xixi')