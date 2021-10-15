#include <stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node* left,*right;
};
void create(struct node **p,int n)
{
    struct node* new=(struct node*)malloc(sizeof(struct node));
    struct node *q=*p;
    new->data=n;
    new->left=NULL;
    new->right=NULL;
    if(*p==NULL)
    {
        *p=new;
    }
    else if(q->data>n)
    create(&(q->left),n);
    else
     create(&(q->right),n);
    
}
void preorder(struct node *p)
{
    if(p!=NULL)
    {
        printf("%d ",p->data);
        preorder(p->left);
        preorder(p->right);
    }
}
void find_and_replace(struct node**p,int n,int ele)
{
    struct node *q=*p;
    if(q!=NULL)
    {
        if(q->data==n)
        {
            q->data=ele;
        }
        find_and_replace(&(q->left),n,ele);
        find_and_replace(&(q->right),n,ele);
    }
    
}
int main()
{
    struct node *p=NULL;
    int n,num,ele,nele;
    printf("How many numbers to insert into BST:");
    scanf("%d",&n);
    printf("\nEnter %d numbers:",n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&num);
        create(&p,num);
        
    }
    printf("\nPreorder(before):");
    preorder(p);
    printf("\nEnter an existing value to replace:");
    scanf("%d",&ele);
    printf("\nEnter new value:");
    scanf("%d",&nele);
    find_and_replace(&p,ele,nele);
    printf("\nPreorder(after):");
    preorder(p);
    return 0;
}
