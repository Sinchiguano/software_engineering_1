public class simpleClass {


	private String girlName;


	public void setName(String name){
		girlName=name;
	}
	public String getName(){
		return girlName;
	}
	public void saying()
	{
		System.out.printf("Your first girlfriend was %s /n", getName());
	}


	public void message(String name)
	{
		System.out.println(name);
	}
	
}