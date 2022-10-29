#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int fn, ws, ps, r[10], j = 0;

struct frame
{
    char ack;
    int data;
} frm[10];

int sender();
void receiveack();
void resend_sr();
void selective();

int main()
{
    int ch;
    selective();
}

void selective()
{
    sender();
    receiveack();
    resend_sr();
    printf("\nAll frames sent successfully");
}

int sender()
{
    int i;

    printf("\nEnter the number of frames to be sent:");
    scanf("%d", &fn);

    for (i = 1; i <= fn; i++)
    {
        printf("Enter data for frame %d : ", i);
        scanf("%d", &frm[i].data);
        frm[i].ack = 'y';
    }
    printf("Enter the window size: ");
    scanf("%d", &ws);
    printf("Enter packet size: ");
    scanf("%d", &ps);
    int c = 0;
    for (i = 1; i <= ps + c; i++)
    {
        if ((i - c) > ws)
        {
            r[j] = i;
            frm[i].ack = 'n';
            j++;
        }
        if (i == ps + c && i < fn)
        {
            c = ps + c;
        }
        if (i > fn)
        {
            break;
        }
    }

    return 0;
}

void receiveack()
{
    int i;
    rand();
label:
    r[j] = rand() % fn;
    if (r[j] == 0)
        goto label;

    frm[r[j]].ack = 'n';
    j++;
    for (i = 1; i <= fn; i++)
    {
        if (frm[i].ack == 'n')
        {
            printf("\nThe frame number %d is not received\n", i);
        }
    }
}

void resend_sr()
{
    int i;
    for (i = 0; i < j; i++)
        printf("r-->%d\n", r[i]);
    for (i = 0; i < j; i++)
    {
        printf("\nResending frame %d\n", r[i]);
        frm[r[j]].ack = 'y';
    }
    sleep(2);

    for (i = 0; i < j; i++)
        printf("\nThe frame %d with data %d is recieved", r[i], frm[r[i]].data);
}
