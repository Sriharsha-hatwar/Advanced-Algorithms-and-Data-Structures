import java.io.Serializable;

public class Student implements Serializable
{
	private String usn;
	private double cgpa;
	
	public Student(String s, double d)
	{
		usn = s;
		cgpa = d;
	}
	
	public String getUsn()
	{
		return this.usn;
	}
	public void setUsn(String s)
	{
		this.usn = s;
	}
	
	public double getCgpa()
	{
		return this.cgpa;
	}
	public void setCgpa(double d)
	{
		this.cgpa = d;
	}
}
