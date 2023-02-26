/**

*/
package sdk.model.transform;

import java.math.*;

import javax.annotation.Generated;

import sdk.model.*;
import com.amazonaws.transform.SimpleTypeJsonUnmarshallers.*;
import com.amazonaws.transform.*;

import com.fasterxml.jackson.core.JsonToken;
import static com.fasterxml.jackson.core.JsonToken.*;

/**
 * UnstructuredMessage JSON Unmarshaller
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
public class UnstructuredMessageJsonUnmarshaller implements Unmarshaller<UnstructuredMessage, JsonUnmarshallerContext> {

    public UnstructuredMessage unmarshall(JsonUnmarshallerContext context) throws Exception {
        UnstructuredMessage unstructuredMessage = new UnstructuredMessage();

        int originalDepth = context.getCurrentDepth();
        String currentParentElement = context.getCurrentParentElement();
        int targetDepth = originalDepth + 1;

        JsonToken token = context.getCurrentToken();
        if (token == null)
            token = context.nextToken();
        if (token == VALUE_NULL) {
            return null;
        }

        while (true) {
            if (token == null)
                break;

            if (token == FIELD_NAME || token == START_OBJECT) {
                if (context.testExpression("id", targetDepth)) {
                    context.nextToken();
                    unstructuredMessage.setId(context.getUnmarshaller(String.class).unmarshall(context));
                }
                if (context.testExpression("text", targetDepth)) {
                    context.nextToken();
                    unstructuredMessage.setText(context.getUnmarshaller(String.class).unmarshall(context));
                }
                if (context.testExpression("timestamp", targetDepth)) {
                    context.nextToken();
                    unstructuredMessage.setTimestamp(context.getUnmarshaller(String.class).unmarshall(context));
                }
            } else if (token == END_ARRAY || token == END_OBJECT) {
                if (context.getLastParsedParentElement() == null || context.getLastParsedParentElement().equals(currentParentElement)) {
                    if (context.getCurrentDepth() <= originalDepth)
                        break;
                }
            }
            token = context.nextToken();
        }

        return unstructuredMessage;
    }

    private static UnstructuredMessageJsonUnmarshaller instance;

    public static UnstructuredMessageJsonUnmarshaller getInstance() {
        if (instance == null)
            instance = new UnstructuredMessageJsonUnmarshaller();
        return instance;
    }
}
