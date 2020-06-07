# IED-tranport-sim

This simulator is designed for IED transportation question Summer 2020 @ RPI

## Transportation Challenge
This section is excerpted from IED *Virtual Mini-Projects* by The Design Lab at Rensselaer.

### Problem Statement
A transportation company must carry a load of medical supplies via truck from the Port of San Diego to Albany Medical Center. Ignore air resistance, rolling resistance & internal vehicle losses, weather, driver needs (food, bathrooms), Tucking Rules and Regulations (FMCSA), and most other things that make this problem complicated. 

Consider size and weight of power source(s) and fuel, but ignore drivetrain and other mounting issues. IE: Removing the gasoline engine from stock Transit van ‘saves’ 449 lbs off vehicle curb weight. Adding the electric motors ‘costs’ 150 lbs. Each rocket motor ‘costs’ 5.5 lbs. Rocket launch controller can fit within drivers pocket and does not impact available cargo size/weight.
Vehicle should not stop along the way, so journey must begin with all required fuel. Consider weight and size of extra tank, gasoline, and how it changes over duration of trip. Consider weight of extra batteries and/or solar panels, and how long sun is out (ignore clouds and weather). 

Students may choose any combination of cargo, power source, and route. The goal is to minimize travel time and maximize supplies delivered.
State ALL additional assumptions and simplifications made (realities ignored) to justify solution presented.
Requires some physics, planning, and iterative ‘simulation’.

### Assumptions
- Your vehicle is a Ford Transit T150 Cargo Van (Long-EL high roof) and U-Haul 6x12 cargo trailer. 
    - https://www.ford.com/commercial-trucks/transit-cargo-van/models/transit-van/
    - https://www.uhaul.com/Trailers/6x12-Cargo-Trailer-Rental/RV/ 
- Federal government has built three new 4 lane straight roadways of various elevation changes. (Don’t ask how this happened from a political, budgetary, or topographical standpoint. Just know that many spherical cows were involved.)
    - A.Perfectly flat, straight-as-the-crow-flies from San Diego CA to Albany NY
    - B.Uphill to US Four Corners Monument (36°59′56.325″N, 109°2′42.67″W) then downhill to Albany NY
    - C.Straight-as-the-crow-flies from San Diego CA to Albany NY (1/2 mile south of route A) with 22 evenly spaced symmetrical hills 2 miles up each side at 3% incline.
- Power source choices, any combination of:
    - Stock 3.5L EcoBoost V6 gasoline engine and 25-gallon tank - qty 1 @ 449 lbs. 
    - Tesla Model S P90D electric motors and 90kWh battery - qty 2 @ 70 lbs. each
    - size L rocket motors – qty TBD @ 5.5 lbs. each 
    https://www.apogeerockets.com/Rocket_Motors/Cesaroni_Propellant_Kits/54mm_Motors/6XL-Grain_Motors/Cesaroni_54-6GXL_Mellow_L265 
- Fuel source choices
    - Standard 25-gallon tank + size/weight cost for additional capacity
    - Standard 90 kWh battery + size/weight cost for additional battery or solar system
    - Rocket launch controller
- Cargo choices:
    - 3M N-95 masks (20 pack) – box 5.625 x 5.625 x 8”, 0.525 lbs.
    - Hamilton C3 ventilator – box (without stand) 24” x 12” x 24”, 25 lbs.
- Trip will begin August 31st 2020 at noon PST.

### Acknowledgements
Our thanks to design Lab Project Engineer Aren Paster for the inspiration and writeup for this project.

## Links
Specification: https://docs.google.com/document/d/1LaZNvKz1YIbP27I2U86Uc2ULOIZnb1hrEGtUMGBAbYU/edit?usp=sharing
