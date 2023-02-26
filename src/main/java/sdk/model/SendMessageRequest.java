/**

*/
package sdk.model;

import java.io.Serializable;
import javax.annotation.Generated;

/**
 * 
 * @see <a href="http://docs.aws.amazon.com/goto/WebAPI/ycp30j8f38-1.0.0/SendMessage" target="_top">AWS API
 *      Documentation</a>
 */
@Generated("com.amazonaws:aws-java-sdk-code-generator")
public class SendMessageRequest extends com.amazonaws.opensdk.BaseRequest implements Serializable, Cloneable {

    private BotRequest botRequest;

    /**
     * @param botRequest
     */

    public void setBotRequest(BotRequest botRequest) {
        this.botRequest = botRequest;
    }

    /**
     * @return
     */

    public BotRequest getBotRequest() {
        return this.botRequest;
    }

    /**
     * @param botRequest
     * @return Returns a reference to this object so that method calls can be chained together.
     */

    public SendMessageRequest botRequest(BotRequest botRequest) {
        setBotRequest(botRequest);
        return this;
    }

    /**
     * Returns a string representation of this object. This is useful for testing and debugging. Sensitive data will be
     * redacted from this string using a placeholder value.
     *
     * @return A string representation of this object.
     *
     * @see java.lang.Object#toString()
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        if (getBotRequest() != null)
            sb.append("BotRequest: ").append(getBotRequest());
        sb.append("}");
        return sb.toString();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;

        if (obj instanceof SendMessageRequest == false)
            return false;
        SendMessageRequest other = (SendMessageRequest) obj;
        if (other.getBotRequest() == null ^ this.getBotRequest() == null)
            return false;
        if (other.getBotRequest() != null && other.getBotRequest().equals(this.getBotRequest()) == false)
            return false;
        return true;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int hashCode = 1;

        hashCode = prime * hashCode + ((getBotRequest() == null) ? 0 : getBotRequest().hashCode());
        return hashCode;
    }

    @Override
    public SendMessageRequest clone() {
        return (SendMessageRequest) super.clone();
    }

    /**
     * Set the configuration for this request.
     *
     * @param sdkRequestConfig
     *        Request configuration.
     * @return This object for method chaining.
     */
    public SendMessageRequest sdkRequestConfig(com.amazonaws.opensdk.SdkRequestConfig sdkRequestConfig) {
        super.sdkRequestConfig(sdkRequestConfig);
        return this;
    }

}
