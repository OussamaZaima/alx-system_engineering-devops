#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - A function that runs infinitely
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry to a program that creats 5 zombie processes
 * Return: Always 0
*/
int main(void)
{
	int child_processes = 0;
	pid_t zombie;

	while (child_processes < 5)
	{
		zombie = fork();
		if (!zombie)
			break;
		printf("Zombie process created, PID: %i\n", zombie);
		child_processes++;
	}
	if (zombie != 0)
		infinite_while();
	return (0);
}
