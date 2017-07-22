import java.io.Serializable;

public class BTree
{
	private TNode root;
	private int t = 2;
		
	private class TNode implements Serializable
	{
		int keyCount = 0;
		boolean leaf = false;		
		Student[] key = new Student[2*t];
		TNode[] ref = new TNode[2*t+1];
	}
	
	public void search(String k)
	{
		search(root, k);
	}
	private void search(TNode node, String k)
	{
		int i = 1;
		while(i<=node.keyCount && k.compareTo(node.key[i].getUsn())>0)
		{	
			i++;
		}
		if(i<=node.keyCount && k.compareTo(node.key[i].getUsn()) == 0)
		{
			System.out.println("USN : " + k + ";CGPA : " + node.key[i].getCgpa());
			return;
		}
		else if(node.leaf)
		{
			System.out.println("No record found on USN : " + k);
			return;
		}
		else
		{
			search(node.ref[i], k);
		}
	}
	
	private void createTree()
	{
		TNode x = new TNode();
		x.leaf = true;
		x.keyCount = 0;
		root = x;
	}
	
	private void splitChild(TNode parent, int pos)
	{
		TNode nChild = new TNode();
		TNode pChild = parent.ref[pos];
		nChild.leaf = pChild.leaf;
		nChild.keyCount = t-1;
		for(int i=1; i<t; i++)
		{
			nChild.key[i] = pChild.key[i+t];
		}
		if(!pChild.leaf)
		{
			for(int i=1; i<=t; i++)
			{	
				nChild.ref[i] = pChild.ref[i+t];
			}
		}
		pChild.keyCount = t-1;
		for(int i=parent.keyCount+1; i>pos; i--)
		{
			parent.ref[i+1] = parent.ref[i]; 
		}
		parent.ref[pos+1] = nChild;
		for(int i=parent.keyCount; i>=pos; i--)
		{
			parent.key[i+1] = parent.key[i];
		}
		parent.key[pos] = pChild.key[t];
		parent.keyCount += 1;		
	}
	
	private void insertNonfull(TNode node, Student k)
	{
		int i = node.keyCount;
		if(node.leaf)
		{
			while(i>=1 && k.getUsn().compareTo(node.key[i].getUsn())<0)
			{
				node.key[i+1] = node.key[i];
				i = i-1;
			}
			node.key[i+1] = k;
			node.keyCount += 1;
		}
		else
		{
			while(i>=1 && k.getUsn().compareTo(node.key[i].getUsn())<0)
			{	
				i = i-1;
			}
			i = i+1;
			if(node.ref[i].keyCount == 2*t-1)
			{
				splitChild(node, i);
				if(k.getUsn().compareTo(node.key[i].getUsn())>0)
				{
					i = i+1;
				}
			}
			insertNonfull(node.ref[i], k);
		}
	}
	
	public void insert(Student k)
	{
		if(root == null)
		{
			createTree();
		}
		TNode r = root;
		if(r.keyCount == 2*t-1)
		{
			TNode s = new TNode();
			root = s;
			s.ref[1] = r;
			splitChild(s, 1);
			insertNonfull(s, k);
		}		
		else
		{
			insertNonfull(r, k);
		}
	}	
	
	private void deleteRecursively(TNode node, int i)
	{
		if(!node.leaf)
		{
			if(node.ref[i].keyCount > t-1)
			{
				node.key[i] = node.ref[i].key[node.ref[i].keyCount];
				deleteRecursively(node.ref[i], node.ref[i].keyCount);	
			}
			else if(node.ref[i+1].keyCount > t-1)
			{
				node.key[i] = node.ref[i+1].key[1];
				deleteRecursively(node.ref[i], 1);
			}
			else
			{	
				TNode pChild = node.ref[i];
				TNode nChild = node.ref[i+1];
				for(int j=1; j<t; j++)
				{
					pChild.key[t+j] = nChild.key[j];
				}
				if(!pChild.leaf)
				{
					for(int j=1; j<=t; j++)
					{
						pChild.ref[t+j] = nChild.ref[j];
					}
				}
				pChild.key[t] = node.key[i]; 
				pChild.keyCount = 2*t-1; 
				for(int j=i+1; j<node.keyCount+1; j++)
				{
					node.ref[j] = node.ref[j+1];
				}
				for(int j=i; j<node.keyCount; j++)
				{
					node.key[j] = node.key[j+1];
				}
				node.keyCount -= 1;
				deleteRecursively(node.ref[i], t);
			}
		}
		else
		{
			while(i<node.keyCount)
			{
				node.key[i] = node.key[i+1];
			}
			node.keyCount -= 1;
		}
	}
	
	private void adjustSubtree(TNode node, int i)
	{
		if(node.ref[i].keyCount < t)
		{
			TNode child = node.ref[i];
			if(node.ref[i-1] != null && node.ref[i-1].keyCount > t-1)
			{
				TNode pSibling = node.ref[i-1];
				for(int k=child.keyCount; k>=1; k--)
				{
					child.key[k+1] = child.key[k];
				}	
				for(int k=child.keyCount+1; k>1; k--)
				{	
					child.ref[k+1] = child.ref[k];
				}
				child.key[1] = node.key[i-1];
				node.key[i-1] = pSibling.key[pSibling.keyCount];
				child.ref[1] = pSibling.ref[pSibling.keyCount+1];
				child.keyCount += 1;
				pSibling.keyCount -= 1;
			}
			else if(node.ref[i+1] != null && node.ref[i+1].keyCount > t-1)
			{
				TNode nSibling = node.ref[i+1];
				child.key[child.keyCount+1] = node.key[i];
				node.key[i] = nSibling.key[1];
				child.keyCount += 1;
				child.ref[child.keyCount+1] = nSibling.ref[1];
				for(int k=1; k>nSibling.keyCount; k--)
				{
					nSibling.key[k] = nSibling.key[k+1];
				}	
				for(int k=1; k>=nSibling.keyCount; k--)
				{	
					nSibling.ref[k] = nSibling.ref[k+1];
				}
				nSibling.keyCount -= 1;
			}
			else
			{
				int k;
				if(node.ref[i-1] != null)
				{
					k = i-1;
				}
				else k = i+1;
				TNode sibling = node.ref[k];
				for(int j=1; j<t; j++)
				{
					child.key[t+j] = sibling.key[j];
				}
				if(!child.leaf)
				{
					for(int j=1; j<=t; j++)
					{
						child.ref[t+j] = sibling.ref[j];
					}
				}
				child.key[t] = node.key[i]; 
				child.keyCount = 2*t-1; 
				for(int j=i+1; j<node.keyCount+1; j++)
				{
					node.ref[j] = node.ref[j+1];
				}
				for(int j=i; j<node.keyCount; j++)
				{
					node.key[j] = node.key[j+1];
				}
				node.keyCount -= 1;	
			}
		}
	}

	private void delete(TNode node, String k)
	{
		int i = node.keyCount;
		while(i>=1 && k.compareTo(node.key[i].getUsn())<0)
		{
			i--;
		}
		if(i<=node.keyCount && k.compareTo(node.key[i].getUsn()) == 0)
		{
			if(node.leaf)
			{
				while(i<node.keyCount)
				{
					node.key[i] = node.key[i+1];
					i++;
				}
				node.keyCount -= 1;
			}
			else 
			{
				deleteRecursively(node, i);
			}
		}
		else if(!node.leaf)
		{
			i = i+1;
			adjustSubtree(node, i);
			delete(node.ref[i], k);
		}
	}
	public void delete(String k)
	{
		delete(root, k);
		if(root.keyCount == 0)
		{
			root = root.ref[1];
		}
	}
}


