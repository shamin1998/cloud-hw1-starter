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
 * Message JSON Unmarshaller
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
public class MessageJsonUnmarshaller implements Unmarshaller<Message, JsonUnmarshallerContext> {

    public Message unmarshall(JsonUnmarshallerContext context) throws Exception {
        Message message = new Message();

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
                if (context.testExpression("type", targetDepth)) {
                    context.nextToken();
                    message.setType(context.getUnmarshaller(String.class).unmarshall(context));
                }
                if (context.testExpression("unstructured", targetDepth)) {
                    context.nextToken();
                    message.setUnstructured(UnstructuredMessageJsonUnmarshaller.getInstance().unmarshall(context));
                }
            } else if (token == END_ARRAY || token == END_OBJECT) {
                if (context.getLastParsedParentElement() == null || context.getLastParsedParentElement().equals(currentParentElement)) {
                    if (context.getCurrentDepth() <= originalDepth)
                        break;
                }
            }
            token = context.nextToken();
        }

        return message;
    }

    private static MessageJsonUnmarshaller instance;

    public static MessageJsonUnmarshaller getInstance() {
        if (instance == null)
            instance = new MessageJsonUnmarshaller();
        return instance;
    }
}
