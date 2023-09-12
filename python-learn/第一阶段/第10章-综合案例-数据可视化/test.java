package par.graph;

import com.graphdbapi.GraphLogger;
import com.graphdbapi.Graph;
import com.graphdbapi.procedure.Context;
import com.graphdbapi.procedure.Name;
import com.graphdbapi.procedure.UserFunction;

public class ScalarTest {

    @Context
    public Graph graph;

    @Context
    public GraphLogger log;

    @UserFunction
    public long valueAdd(@Name("value") Long value) {
        log.info("value add");
        return value + 10;
    }

}
StatementResult statementResult = graph.executeQuery("match (n:个人) where par.graph.valueAdd(n.评分) > 10 return n");
while (statementResult.hasNext()) {
    Record next = statementResult.next();
    System.out.println(next.get(0).asNode());
}