from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank= True)
    # creates a default image/every model that we don't add an image for is going to have the default pic until we modify it   
    featured_image = models.ImageField(null = True, blank= True, default = "default.jpeg")
    demo_link = models.CharField(max_length= 2000, null = True, blank= True)
    source_link = models.CharField(max_length=2000, null = True, blank= True)
    tags = models.ManyToManyField('Tag', blank = True) # True means we dont need to select a tag #create a relationship to a tag (tag can be connected to multiple models)
    vote_total = models.IntegerField(default=0, null=True, blank=True)#store votes here
    vote_ratio= models.IntegerField(default=0, null=True, blank=True)#store votes here
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid. uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (   #creating a tuple reference by using 'up' but 'Up Vote' is what is displayed
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner = 
    project = models.ForeignKey(Project, on_delete= models.CASCADE) #(on_delete, whenever a project is deleted what do we want to do with all the children, all the reviews connected to the project) here, if a project is deleted the review will be left alone and the project field is set to SET_NULL (CASCADE will delete all reviews if project is deleted)
    body =  models.TextField(null = True, blank= True)    #when someoe writes a review 
    value = models.CharField(max_length=200, choices=VOTE_TYPE)    #give user only two options, dont want them to write anything (This will be a dropdown list)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid. uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value  #return the vote

#create a many to many relationship
#created and ID is consistant thoughout all our models 
class Tag(models.Model): #inherit from model
    name = models.CharField(max_length=200) #name of tag
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid. uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name