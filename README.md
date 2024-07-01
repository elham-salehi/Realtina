# Realtyna

# Django Reservation Project

This project is a Django-based reservation project that can be used by multiple listings. It provides REST API endpoints for making reservations, checking a number of rooms availability, and generating reports in HTML format.

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/elham-salehi/realtyna.git
    cd realtyna
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
   
5. **Run the development server**:

    ```sh
    python manage.py runserver
    ```

## API Endpoints

### 1. Make a Reservation

**Endpoint**: `POST /realtyna/reservations/`

**Description**: This endpoint allows you to create a new reservation for a number of rooms, guest name, and time period.

**Request Body**:
- `guest_name` (string): Name of the guest making the reservation.
- `booked_rooms` (positive integer): Number of rooms reservation.
- `check_in` (datetime): Check in time.
- `check_out` (datetime): Check out time.
- `list` (List): The related list for rooms.


    
### 2. Check availability of a number of rooms in a certain time

**Endpoint**: `GET /realtyna/lists/{list_id}/bookable/`

**Description**: This endpoint checks if a number of rooms are available for a certain time.

**Path Parameter**:

- `list_id` (integer): The ID of the list we want to check a number of rooms availability.

**Query Parameters**:
- `check_in` (datetime): Check in time of the desired reservation period.
- `check_out` (datetime): Check out time of the desired reservation period.
- `rooms` (positive integer) : Number of rooms for check availability


### 3. Get Reservations Report

**Endpoint**: `GET /realtyna/report/`

**Description**: This endpoint generates a report of all reservations in HTML.

