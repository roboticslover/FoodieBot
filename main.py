import streamlit as st


def main():
    # Set background color
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6; /* Light gray background */
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #222831; /* Dark background */
            color: #ffffff; /* White text */
            text-align: center;
            padding: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and introduction
    st.title("Welcome to FoodieBot 🍔")
    st.subheader("Your Personal Food Ordering Assistant")

    # Instructions for using the chatbot
    st.markdown("### Instructions:")
    st.markdown("1. Type 'Hey' to start.")
    st.markdown("2. Enter 'New Order' to begin a new order.")
    st.markdown(
        "3. Add food items by typing their names from the menu and specify the quantity also.")
    st.markdown("4. Remove items with 'Remove [food-item-name]'.")
    st.markdown("5. Enjoy your meal!")

    # Chatbot iframe
    st.markdown(
        """
        <iframe 
            width="100%" 
            height="600" 
            src="https://console.dialogflow.com/api-client/demo/embedded/19e1242a-babb-477e-9621-f2bffe9a9892"
            frameborder="0"
            allow="microphone">
        </iframe>
        """,
        unsafe_allow_html=True
    )

    # Footer
    st.markdown('<div class="footer">Made with ❤️ by [!!!Sachin Singh Rathore!!!]</div>',
                unsafe_allow_html=True)


if __name__ == "__main__":
    main()
