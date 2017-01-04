import java.util.ArrayList;
import java.util.Scanner;
/**
 * Created by xubowen on 2016/12/25.
 */
public class Container {
    private ArrayList arrList = new ArrayList();
    private int LENGTH = Main.bufferCount;
    public boolean isFull() {
        //System.out.println("已经满了");
        return arrList.size() == LENGTH;
    }
    public boolean isEmpty() {
        return arrList.isEmpty();
    }
    public int size(){
        return arrList.size();
    }
    /* 如果此处不加synchronized锁，那么也可以再调用push的地方加锁
    * 既然此处加了锁，那么再别的地方可以不加锁
    */
    public synchronized void push(Object o) {
        arrList.add(o);
    }
    // 如果此处不加synchronized锁，那么也可以再调用push的地方加锁
    public synchronized Object pop() {
        Object lastOne = arrList.get(arrList.size() - 1);
        arrList.remove(arrList.size() - 1);
        return lastOne;
    }
}