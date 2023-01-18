#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// structure for customer
typedef struct Customer
{
    char firstName[50];
    char middleInitial[50];
    char lastName[50];
    char streetAddress[50];
    char city[50];
    char state[50];
    char zipCode[50];
    char country[50];
    char emailAddress[50];
    char telephoneNumber[50];
    char gender[20];
    char dateOfBirth[50];
} Customer;

Customer customerArray[1000]; // global Customer array

// global variable to keep track of the number of customers
int numberOfCustomers = 0;

void generateCustomerArray()
{
    // open the file
    FILE *fp;
    fp = fopen("customerData.txt", "r");

    if (fp == NULL) // if error in opening file
    {
        printf("Error opening file customerData.txt");
        exit(1);
    }

    // read the file line by line
    char *line = NULL;
    ssize_t read;
    size_t len = 0;

    while ((read = getline(&line, &len, fp)) != -1)
    {
        // Split Line Across Commas
        char *data = strtok(line, ",");

        // Create Temp Customer
        Customer temp;

        // Represent Struct data to store
        int index = 1;
        while (data != NULL)
        {
            switch (index)
            {
            case 1:
                strcpy(temp.firstName, data);
                break;
            case 2:
                strcpy(temp.middleInitial, data);
                break;
            case 3:
                strcpy(temp.lastName, data);
                break;
            case 4:
                strcpy(temp.streetAddress, data);
                break;
            case 5:
                strcpy(temp.city, data);
                break;
            case 6:
                strcpy(temp.state, data);
                break;
            case 7:
                strcpy(temp.zipCode, data);
                break;
            case 8:
                strcpy(temp.country, data);
                break;
            case 9:
                strcpy(temp.emailAddress, data);
                break;
            case 10:
                strcpy(temp.telephoneNumber, data);
                break;
            case 11:
                strcpy(temp.gender, data);
                break;
            case 12:
                strcpy(temp.dateOfBirth, data);
                break;
            default:
                break;
            }
            data = strtok(NULL, ",");
            index++;
        }

        // Store Temp customer into array of customers
        customerArray[numberOfCustomers] = temp;
        numberOfCustomers++;
    }

    // Close File
    fclose(fp);
}

void produceMailingLabels()
{

    // Create File to save data
    FILE *fp = fopen("mailingLabels.txt", "w");
    if (fp == NULL)
    {
        printf("Error opening the file");
        return;
    }

    // print the total number of customers
    // printf("Total number of customers: %d \n", numberOfCustomers);

    // Loop Through all customers and save record in a file
    for (int i = 0; i < numberOfCustomers; i++)
    {
        if (strcmp(customerArray[i].gender, "female") == 0 && (strcmp(customerArray[i].state, "IA") == 0 || strcmp(customerArray[i].state, "NE") == 0))
        {

            // Save in File

            fputs(customerArray[i].firstName, fp);
            fputs(" ", fp);
            fputs(customerArray[i].lastName, fp);
            fputs("\n", fp);
            fputs(customerArray[i].streetAddress, fp);
            fputs("\n", fp);
            fputs(customerArray[i].city, fp);
            fputs(",", fp);
            fputs(customerArray[i].state, fp);
            fputs(" ", fp);
            fputs(customerArray[i].zipCode, fp);
            fputs("\n\n\n\n\n", fp);
        }
    }

    // close the file
    fclose(fp);
}

int main()
{
    generateCustomerArray();
    produceMailingLabels();
    return 0;
}