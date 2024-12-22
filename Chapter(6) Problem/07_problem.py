# Write a program to find out whether a given post is talking alout "faiz" or not.
post = input("Enter the post: ")

# if("faiz" in post.lower()):

if("Faiz".lower() in post.lower()):
    print("This post is talking about faiz")

else:
    print("This post is not talking about faiz")