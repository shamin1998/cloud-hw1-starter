/**

*/
package sdk;

import javax.annotation.Generated;

import com.amazonaws.*;
import com.amazonaws.opensdk.*;
import com.amazonaws.opensdk.model.*;
import com.amazonaws.regions.*;

import sdk.model.*;

/**
 * Interface for accessing DiningConcierge.
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
public interface DiningConcierge {

    /**
     * @param sendMessageRequest
     * @return Result of the sendMessage operation returned by the service.
     * @throws InternalServerErrorException
     * @throws ForbiddenException
     * @sample DiningConcierge.sendMessage
     * @see <a href="http://docs.aws.amazon.com/goto/WebAPI/ycp30j8f38-1.0.0/sendMessage" target="_top">AWS API
     *      Documentation</a>
     */
    SendMessageResult sendMessage(SendMessageRequest sendMessageRequest);

    /**
     * @return Create new instance of builder with all defaults set.
     */
    public static DiningConciergeClientBuilder builder() {
        return new DiningConciergeClientBuilder();
    }

    /**
     * Shuts down this client object, releasing any resources that might be held open. This is an optional method, and
     * callers are not expected to call it, but can if they want to explicitly release any open resources. Once a client
     * has been shutdown, it should not be used to make any more requests.
     */
    void shutdown();

}
