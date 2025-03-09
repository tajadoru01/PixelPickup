# PixelPickup - AI-Powered Return Assessment System
## Team Mingjd - Hack the Future

### Overview

PixelPickup is an AI-powered return assessment system that streamlines the product return process. By utilizing Google’s Gemini API for image analysis and OpenRouteService for geolocation tracking, PixelPickup helps customers determine whether their items can be returned to a store, donated, or recycled.

### Features
 - **AI-Powered Classification:** Customers upload an image of their product, and our system determines the most suitable return option.
 - **Seamless Return Guidance:** Based on the assessment, users receive return instructions for store drop-off, donation, or recycling.
 - **Real-Time Mapping:** OpenRouteService provides dynamic routing and driver tracking for returns and pickups.
 - **Error Handling:** If an uploaded image isn’t recognized as a valid returnable item, an error message is displayed with guidance for next steps.

### How it Works

1. Image Upload & Processing: Customers upload an image of the item they wish to return.

2. AI Classification: The system categorizes the item into one of the following return options:

      - Return to Store: If the product meets store return criteria (e.g., within a 30-day window, original tags attached, unworn condition), the system provides store return details and estimated refunds.

      - Donate: If the product is still usable but ineligible for store return, the system suggests donation options to support local communities and reduce waste.

      - Recycle: If the product is non-returnable but recyclable, the system directs customers to local recycling centers for sustainable disposal.

      - Error Case: If the uploaded image is unrecognizable or not related to clothing, the system alerts the customer with an error message.

 3. Mapping & Logistics: For eligible returns, OpenRouteService provides:

      - Optimal route calculation for pickup/drop-off locations.

      - An interactive map displaying the driver’s location relative to the customer.

      - Real-time updates on estimated arrival times.
   
### Installation & Setup

1. Clone the repository
2. Install dependencies
3. Set up API keys for Google Gemini API and OpenRouteService in a .env file
     - GEMINI_API_KEY=your_api_key_here
     - OPENROUTESERVICE_API_KEY=your_api_key_here
4. Start application
   
### Usage
- Upload an image of the product you want to return.

- View the AI-assessed return option (Return, Donate, Recycle, or Error Message).

- Follow the provided instructions for completing the return.

- Track driver location (if applicable) through the interactive map.




