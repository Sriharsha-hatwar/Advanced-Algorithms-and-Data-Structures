import java.util.Scanner;
import java.io.FileInputStream;

public class Client
{
	public static void main(String[] args) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		BTree bt = new BTree();
		int i = 0;
		String file = null;
		String s = null;
		double j = 0.0;
		Student stu = null;
		do
		{
			System.out.println("Choose the following operations:");
			System.out.println("1.Enter a student record");
			System.out.println("2.Enter student records using a file");
			System.out.println("3.Search a student record");
			System.out.println("4.Delete a student record");
			System.out.println("5.Exit");
			i = sc.nextInt();
			switch(i)
			{
				case 1 : System.out.println("Enter the USN and CGPA of the student");
							s = sc.next();
							j = sc.nextDouble();
							stu = new Student(s, j);
							bt.insert(stu);
							break;
				case 2 : System.out.println("Enter the name of the file");
							file = sc.next();
							Scanner fc = new Scanner(new FileInputStream(file));
							while(fc.hasNext())
							{
								s = fc.next();
								j = fc.nextDouble();
								stu = new Student(s, j);
								bt.insert(stu);
							}
							break;
				case 3 : System.out.println("Enter the USN of the student to be searched");
							s = sc.next();
							bt.search(s);
							break;
				case 4 : System.out.println("Enter the USN of the student record to be deleted");			
							s = sc.next();
							bt.delete(s);
							break;
			}
		}while(i!=5);
	}
}
