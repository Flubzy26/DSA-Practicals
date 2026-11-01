#include <iostream>
#include <cstdlib>   // for malloc, realloc, free
#include <cstring>   // for strcmp
using namespace std;

struct Student {
    int roll;
    char name[50];
    float cgpa;
};

// ---------- SEARCH FUNCTIONS ----------

// Linear search by roll number
int linearSearch(Student* students, int count, int id) {
    for (int i = 0; i < count; i++) {
        if (students[i].roll == id)
            return i;
    }
    return -1;
}

// Binary search by roll number (requires sorted by roll!)
int binarySearch(Student* students, int count, int id) {
    int low = 0, high = count - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (students[mid].roll == id)
            return mid;
        else if (students[mid].roll < id)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

// ---------- SORTING FUNCTIONS ----------

// Bubble Sort by Name (alphabetical order)
void bubbleSortByName(Student* students, int count) {
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (strcmp(students[j].name, students[j + 1].name) > 0) {
                swap(students[j], students[j + 1]);
            }
        }
    }
}

// Selection Sort by CGPA
void selectionSortByCGPA(Student* students, int count, bool ascending = true) {
    for (int i = 0; i < count - 1; i++) {
        int idx = i;
        for (int j = i + 1; j < count; j++) {
            if (ascending) {
                if (students[j].cgpa < students[idx].cgpa)
                    idx = j;
            } else {
                if (students[j].cgpa > students[idx].cgpa)
                    idx = j;
            }
        }
        swap(students[i], students[idx]);
    }
}

// ---------- DISPLAY FUNCTION ----------
void displayStudents(Student* students, int count) {
    if (count == 0) {
        cout << "No student data available.\n";
        return;
    }
    cout << "\n--- Student Records ---\n";
    for (int i = 0; i < count; i++) {
        cout << "\nStudent " << i + 1 << ":\n";
        cout << "Roll Number: " << students[i].roll << endl;
        cout << "Name: " << students[i].name << endl;
        cout << "CGPA: " << students[i].cgpa << endl;
    }
    cout << "--------------------------\n";
}

// ---------- MAIN ----------
int main() {
    Student* students = nullptr;
    int count = 0;
    int choice;

    do {
        cout << "\nMenu:\n";
        cout << "1. Add One Student\n";
        cout << "2. Display All Students\n";
        cout << "3. Linear Search by Roll\n";
        cout << "4. Binary Search by Roll (sorted)\n";
        cout << "5. Sort by Name (Bubble Sort)\n";
        cout << "6. Sort by CGPA Ascending (Selection Sort)\n";
        cout << "7. Sort by CGPA Descending (Selection Sort)\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch(choice) {
            case 1: {
                students = (Student*) realloc(students, (count + 1) * sizeof(Student));
                if (students == nullptr) {
                    cout << "Memory allocation failed.\n";
                    exit(1);
                }
                cout << "Enter Roll Number: ";
                cin >> students[count].roll;
                cin.ignore();
                cout << "Enter Name: ";
                cin.getline(students[count].name, 50);
                cout << "Enter CGPA: ";
                cin >> students[count].cgpa;
                count++;
                cout << "\n Student added successfully!\n";
                displayStudents(students, count);
                break;
            }

            case 2:
                displayStudents(students, count);
                break;

            case 3: {
                int id;
                cout << "Enter Roll Number to search (Linear): ";
                cin >> id;
                int idx = linearSearch(students, count, id);
                if (idx != -1) {
                    cout << "\n Student Found:\n";
                    cout << "Roll: " << students[idx].roll 
                         << ", Name: " << students[idx].name 
                         << ", CGPA: " << students[idx].cgpa << endl;
                } else {
                    cout << " Student not found.\n";
                }
                break;
            }

            case 4: {
                int id;
                cout << "Enter Roll Number to search (Binary): ";
                cin >> id;
                // Sort by roll before binary search
                for (int i = 0; i < count - 1; i++) {
                    for (int j = 0; j < count - i - 1; j++) {
                        if (students[j].roll > students[j + 1].roll)
                            swap(students[j], students[j + 1]);
                    }
                }
                int idx = binarySearch(students, count, id);
                if (idx != -1) {
                    cout << "\n Student Found:\n";
                    cout << "Roll: " << students[idx].roll 
                         << ", Name: " << students[idx].name 
                         << ", CGPA: " << students[idx].cgpa << endl;
                } else {
                    cout << " Student not found.\n";
                }
                cout << "\n Current Sorted List by Roll (for verification):\n";
                displayStudents(students, count);
                break;
            }

            case 5:
                bubbleSortByName(students, count);
                cout << "\n Students sorted by Name (Alphabetical).\n";
                displayStudents(students, count);
                break;

            case 6:
                selectionSortByCGPA(students, count, true);
                cout << "\n Students sorted by CGPA (Ascending).\n";
                displayStudents(students, count);
                break;

            case 7:
                selectionSortByCGPA(students, count, false);
                cout << "\n Students sorted by CGPA (Descending).\n";
                displayStudents(students, count);
                break;

            case 8:
                cout << "Exiting program.\n";
                break;

            default:
                cout << "Invalid choice!\n";
        }

    } while(choice != 8);

    free(students);
    return 0;
}
