from property_agent import Agent


agent = Agent()

for count in range(int(input("Amount of properties for purchasing: "))):
    # add property for purchasing
    print('Fill in information about property for purchase:')
    agent.add_property()
# print cheapest
print('Cheapest property:\n')
agent.property_price_purchasing()
print('Most expensive property:\n')
agent.property_price_purchasing(flag = "max")


for count in range(int(input("Amount of properties for renting: "))):
    # add property for renting
    print('Fill in information about property for rent:')
    agent.add_property()
# print cheapest
print('Cheapest property for renting:\n')
agent.property_price_renting()
print('Most expensive property for renting:\n')
agent.property_price_renting(flag = "max")
