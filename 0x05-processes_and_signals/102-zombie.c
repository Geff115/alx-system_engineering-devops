#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - Creates 5 zombie processes and keeps the parent alive.
 *
 * Return: Always 0 success.
 */
int infinite_while(void);

int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == -1)
		{
			perror("fork error\n");
			return (1);
		}
		if (child == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", child);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while: Create a zombie process infinitely until ctrl c is entered by the user..
 *
 * Return: 0 success.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
