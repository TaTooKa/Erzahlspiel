Space Travel
============

.. figure:: /_static/images/rpg-image-24.jpg

   art © `Maciej Rebisz <https://www.artstation.com/mac>`_


Traveling through space is costly, but in the 22nd century, humanity’s advancements in rocket science, nuclear fusion and material technology allow for extremely fast spacecraft and very efficient fuel. With diverse engines capable of thrust in the order of Kilo and Mega Newtons, vessels can get from planetary system to planetary system in a matter of days (instead of months or years), and/or sustain artificial gravity by maintaining constant thrust, provided the crew can afford the fuel costs.

Engine types range from *Nuclear Thermal*, which uses a nuclear reactor to heat a propellant like Liquid Hydrogen or Ammonia and ejects it through the exhaust nozzle to generate thrust, to *Fusion Drives* that use Deuterium, Tritium or Trilium (₃He) for Reaction and propellant.

To simplify matters and don’t bog gametime, the Ships detailed in the Spacecraft section (the most common models in the Solar System) have a listed value of MΔv (Max DeltaV), in Km/s or Mm/s. This represents the total budget for all the changes in velocity a ship would do, by taking into account the engine thrust capabilities, exhaust velocity, and wet and dry mass (ship’s mass with a full tank vs an empty tank). All of these variables are already pre-calculated into the Δv budgets listed in this chapter, for simplicity and expedience.

Fuel Consumption
----------------

Instead of counting fuel tons, it’s easier to calculate costs of Δv, in m/s (usually in the order of Km/s or Mm/s). When planning for a trip, consult in the Travel Time+Δv cost tables to see if you can afford the required Δv budget (must be less than your ship’s remaining Δv budget). After arriving at your destination, subtract the spent Δv from your ship’s total. When you refuel, the ship’s Δv returns to its max DeltaV (MΔv) value.

Refuelling
----------

The only thing you have to take into account is the type of fuel/propellant your engine type uses, because when refuelling, the prices will vary a lot depending on the rarity and availability. When you refuel, divide your MΔv by your remaining Δv to get the percentage of fuel left, then subtract that from your Fuel Tank Capacity and buy the remainder in fuel tons. Or to make things easier (and if saving money is not a concern), assume you spent all of your fuel and fill the tank from 0% to 100% by paying the total cost of required fuel tons.

Traveling through Space
-----------------------

Before the current advancements in engine types, spacecraft would use every trick in the book to travel through space: Hohmann Transfers (Orbital assists), Oberth Maneuvers (gravity-assisted slingshots), Bi-Elliptic Transfers, etc. These saved lots of Δv in a time where the current costs were prohibitive or outright impossible. It also meant transit times were extremely long (months or even years) because of all the (literal) hoops a ship would have to do around celestial objects and the fact that they would have to wait for specific launch windows or the correct/optimal position of planets in the system.

Luckily, in the 22nd century, all of that is no longer necessary. Any space-worthy vessel has the means to basically travel in a straight line from planetary system to system, either by accelerating+coasting+decelerating, or by constantly accelerating+decelerating to their destination. All of the techniques from the past are still used from time to time, but only by specific craft or missions that can afford longer times of arrival or that don’t have the economic means to pay for better engines or their fuel (these are mostly educational or science craft from developing nations or crafty enthusiasts).

Outside of those earlier techniques, nowadays most if not all spacecraft use what is called a **Full** or **Partial Brachistochrone**.

.. figure:: /_static/images/rpg-image-25.jpg

   art © `Glenn Clovis <https://www.artstation.com/glenn_clovis>`_


Full Brachistochrone Transit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The vessel accelerates at a constant **g** until the midpoint, turns around and decelerates at the same constant g until its destination. Consult the tables on the following pages of this chapter for already calculated figures and Δv costs for common transit routes and Gs.

If you wish to calculate the Δv cost and transit times on your own, you can use these kinematic formulas:

.. math:: 

   \Delta v \ cost = 2\sqrt{distance * acceleration}

.. math:: 

   Transit \ Time = 2\sqrt{\frac{distance}{acceleration}}

**Δv cost** will be in m/s; **distance** is in m; **acceleration** is in m/s; **Transit time** is in s.

.. epigraph:: Full Brachistochrone Transit Example

   *A character wants to get from the Earth system to Mars (0.52 AU) at a leisure 0.5g of acceleration. The player converts those values for the calculations into metric units and gets a distance of 7,779,089,2764m and an acceleration of 4.9 m/s². Plugging those values into the aforementioned equations solves for a Δv cost of 1,235,206 m/s (1.2Mm/s) and a transit time of 251,912s (70 hours, or 2.9 days).*

The advantages of a Full Brachistochrone are many: The crew is under stable gravity because of constant thrust, that they can set to a comfortable one and avoid all of the problems of long exposure to zero-G; Transit time is reduced, which is not only convenient for those in a hurry, but also reduces time exposure to background radiation and potential Solar Storms or Flares.

The main disadvantage is one of cost (Propellants and Fusion fuel are expensive), and that even the most powerful of the available craft still have their limits, making some trips at high G prohibitive (Δv cost-wise) even at full burn (if the high-G exposure doesn’t kill the crew first!).

Partial Brachistochrone Transit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The vessel accelerates for a period of time at a constant g, then drifts in 0g for another period, then decelerates for another period at a constant g. This saves fuel (in the form of Δv) at the cost of extra time in transit.

In order to calculate time and Δv cost for a Partial Brachistochrone, first decide what percentage of the trip you will be under thrust (in two segments: accelerating, then decelerating), and what percentage you will be coasting at 0g.

.. math:: 

   Reduced \ \Delta v \ cost = 2\sqrt{\frac{acceleration * distance * thrust\ \%}{1 - thrust\ \%}}

.. math:: 

   Increased \ Transit \ Time = \sqrt{\frac{distance}{acceleration * thrust\ \% * (1 - thrust\ \%)}}

**Δv cost** is in m/s; **distance** is in m; **acceleration** is in m/s; **Transit time** is in s; **thrust %** is in decimal form (i.e: 30% is 0.3) for **each** thrust segment.

.. epigraph:: Partial Brachistochrone Transit Example

   *The character realizes that his trip to the Mars System is unattainable on his Light Freighter (that has a maximum Δv of 500 km/s). He decides to do a Partial Brachistochrone instead, at the same acceleration of 0.5g but with only 20% of the trip under thrust. The player needs to convert that fraction into decimal (0.2, divided by two because he needs the value for each thrust segment, which gives a 0.1). Plugging all of those values into the equations gives him a highly reduced Δv cost of 411.74 Km/s (33.3% of the original cost), but an increased total transit time of 4.9 days (almost two days more than if under full burn), and the character’s vessel will be most of that trip coasting at zero-G.*

The advantages of a Partial Brachistochrone are that you save lots of Δv for a relatively small increase in total transit time, and that spacecraft with lesser MΔv capabilities can make trips that could be prohibitive at full burn, by taking a little bit more of time. Many spacers would consider at least short-coasting (10%, 20%) Partial Brachistochrones because they are way more cost-effective than Full Brachistochrones.

The disadvantages are, of course, longer total transit time (submitting the crew to more background radiation exposure and increasing the possibility of living through a Solar Storm in space) and longer time in zero-G, which is not only inconvenient or uncomfortable, but can be a health issue in itself.

Partial Brachistochrone Transit (simplified)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This optional formula is a simplified approximation you can use instead of the previous one. It is not as involved or accurate as the previous one, but will reduce the amount of math required in the game table, while still giving increased transit times for reduced Δv costs.

First decide what percentage of the trip you will be under thrust, and what percentage you will be coasting at 0g. Then multiply the total travel time by 2X the coasting percentage, and divide the DeltaV cost by that thrust percentage. 


.. admonition:: Example of Simplified calculations

   If you travel from Earth to Mars at 0.3g and decide to do 20% burn and 80% coasting, it will take 234.8 hours (90.3 * (1+ (0.8 * 2)), or 160% the duration) and it will cost 191.4 km/s of Δv budget (957 * 0.2, 20% of the original cost).

The simplified formula is:

.. math:: 

   Reduced \Delta v \ cost = \frac{original \Delta v \ cost}{thrust\ time\ percentage}

.. math::

   Increased\ Transit\ Time = original\ transit\ time * (coasting\ time\ percentage * 2) 

Distance between Planetary Systems
----------------------------------

.. csv-table:: Average distance between planetary systems in astronomical units
   :align: center
   :header-rows: 1
   :stub-columns: 1

   "","EARTH SYSTEM","MARS SYSTEM","ASTEROID BELT","JOVIAN SYSTEM","SATURNIAN SYSTEM"
   "EARTH SYSTEM","〰","0.52 AU","1.77 AU","4.2 AU","8.54 AU"
   "MARS SYSTEM","0.52 AU","〰","1.24 AU","3.68 AU","8.02 AU"
   "ASTEROID BELT","1.77 AU","1.24 AU","〰","2.44 AU","6.79 AU"
   "JOVIAN SYSTEM","4.2 AU","3.68 AU","2.44 AU","〰","4.34 AU"
   "SATURNIAN SYSTEM","8.54 AU","8.02 AU","6.79 AU","4.34 AU","〰"

Communication Delay between Planetary Systems
---------------------------------------------

.. csv-table:: Average communication delay between planetary systems in minutes
   :align: center
   :header-rows: 1
   :stub-columns: 1

   "","EARTH SYSTEM","MARS SYSTEM","ASTEROID BELT","JOVIAN SYSTEM","SATURNIAN SYSTEM"
   "EARTH SYSTEM","〰","4 min","15 min","35 min","71 min"
   "MARS SYSTEM","4 min","〰","10 min","31 min","67 min"
   "ASTEROID BELT","15 min","10 min","〰","20 min","56 min"
   "JOVIAN SYSTEM","35 min","31 min","20 min","〰","36 min"
   "SATURNIAN SYSTEM","71 min","67 min","56 min","36 min","〰"

.. warning::

   These comm delays are at a best-case-scenario, probably with military or government priority. Those civilians who can pay the exorbitant amounts of money to have high-priority comms could probably expect 2X or 3X these delays; most common people should probably expect 10X these figures.

Travel Times and DeltaV Costs
-----------------------------

Choose the amount of Gs of acceleration you want to burn at, and check how much time it will take to traverse between Planetary Systems and at what Δv cost.

0.01g of Acceleration
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Average Travel Time and Δv Cost between planetary systems at 0.01G
   :align: center
   :header-rows: 1
   :stub-columns: 1
   :widths: 10, 18, 18, 18, 18, 18

   * - 0.01g
     - EARTH SYSTEM
     - MARS SYSTEM
     - ASTEROID BELT
     - JOVIAN SYSTEM
     - SATURNIAN SYSTEM
   * - EARTH SYSTEM
     - | 
       | 〰
       |
     - | 494.7 h
       | (20.6 days)
       | Δv 174.7 km/s
     - | 912.7 h
       | (38.0 days)
       | Δv 322.3 km/s
     - | 1406.0 h
       | (58.6 days)
       | Δv 496.5 km/s
     - | 2004.9 h
       | (83.5 days)
       | Δv 708.0 km/s
   * - MARS SYSTEM
     - | 494.7 h
       | (20.6 days)
       | Δv 174.7 km/s
     - | 
       | 〰
       | 
     - | 764.0 h
       | (31.8 days)
       | Δv 269.8 km/s
     - | 1316.1 h 
       | (54.8 days)
       | Δv 464.8 km/s
     - | 1942.9 h 
       | (81.0 days)
       | Δv 686.1 km/s
   * - ASTEROID BELT
     - | 912.7 h
       | (38.0 days)
       | Δv 322.3 km/s
     - | 764.0 h
       | (31.8 days)
       | Δv 269.8 km/s
     - | 
       | 〰
       | 
     - | 1071.7 h 
       | (44.7 days)
       | Δv 378.5 km/s
     - | 1787.7 h
       | (74.5 days)
       | Δv 631.3 km/s
   * - JOVIAN SYSTEM
     - | 1406.0 h
       | (58.6 days)
       | Δv 496.5 km/s
     - | 1316.1 h 
       | (54.8 days)
       | Δv 464.8 km/s
     - | 1071.7 h 
       | (44.7 days)
       | Δv 378.5 km/s
     - | 
       | 〰
       | 
     - | 1429.2 h
       | (59.6 days)
       | Δv 504.7 km/s
   * - SATURNIAN SYSTEM
     - | 2004.9 h
       | (83.5 days)
       | Δv 708.0 km/s
     - | 1942.9 h 
       | (81.0 days)
       | Δv 686.1 km/s
     - | 1787.7 h
       | (74.5 days)
       | Δv 631.3 km/s
     - | 1429.2 h
       | (59.6 days)
       | Δv 504.7 km/s
     - | 
       | 〰
       | 

0.1g of Acceleration
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Average Travel Time and Δv Cost between planetary systems at 0.1G
   :align: center
   :header-rows: 1
   :stub-columns: 1
   :widths: 10, 18, 18, 18, 18, 18

   * - 0.1g
     - EARTH SYSTEM
     - MARS SYSTEM
     - ASTEROID BELT
     - JOVIAN SYSTEM
     - SATURNIAN SYSTEM
   * - EARTH SYSTEM
     - | 
       | 〰
       |
     - | 156.4 h 
       | (6.5 days)
       | Δv 552.5 km/s
     - | 288.6 h
       | (12.0 days)
       | Δv 1.0 Mm/s
     - | 444.6 h
       | (18.5 days)
       | Δv 1.6 Mm/s
     - | 634.0 h
       | (26.4 days) 
       | Δv 2.2 Mm/s
   * - MARS SYSTEM
     - | 156.4 h 
       | (6.5 days)
       | Δv 552.5 km/s
     - | 
       | 〰
       | 
     - | 241.6 h
       | (10.1 days)
       | Δv 853.2 km/s
     - | 416.2 h
       | (17.3 days)
       | Δv 1.5 Mm/s 
     - | 614.4 h
       | (25.6 days)
       | Δv 2.2 Mm/s
   * - ASTEROID BELT
     - | 288.6 h
       | (12.0 days)
       | Δv 1.0 Mm/s
     - | 241.6 h
       | (10.1 days)
       | Δv 853.2 km/s
     - | 
       | 〰
       | 
     - | 338.9 h
       | (14.1 days) 
       | Δv 1.2 Mm/s
     - | 565.3 h
       | (23.6 days)
       | Δv 2.0 Mm/s
   * - JOVIAN SYSTEM
     - | 444.6 h
       | (18.5 days)
       | Δv 1.6 Mm/s
     - | 416.2 h
       | (17.3 days)
       | Δv 1.5 Mm/s
     - | 338.9 h
       | (14.1 days)
       | Δv 1.2 Mm/s
     - | 
       | 〰
       | 
     - | 452.0 h
       | (18.8 days)
       | Δv 1.6 Mm/s
   * - SATURNIAN SYSTEM
     - | 634.0 h
       | (26.4 days)
       | Δv 2.2 Mm/s
     - | 614.4 h
       | (25.6 days)
       | Δv 2.2 Mm/s
     - | 565.3 h
       | (23.6 days)
       | Δv 2.0 Mm/s
     - | 452.0 h
       | (18.8 days)
       | Δv 1.6 Mm/s
     - | 
       | 〰
       | 

0.2g of Acceleration
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Average Travel Time and Δv Cost between planetary systems at 0.2G
   :align: center
   :header-rows: 1
   :stub-columns: 1
   :widths: 10, 18, 18, 18, 18, 18

   * - 0.2g
     - EARTH SYSTEM
     - MARS SYSTEM
     - ASTEROID BELT
     - JOVIAN SYSTEM
     - SATURNIAN SYSTEM
   * - EARTH SYSTEM
     - | 
       | 〰
       |
     - | 110.6 h 
       | (4.6 days)
       | Δv 781.4 km/s
     - | 204.1 h
       | (8.5 days)
       | Δv 1.4 Mm/s
     - | 314.4 h
       | (13.1 days)
       | Δv 2.2 Mm/s
     - | 448.3 h
       | (18.7 days)
       | Δv 3.2 Mm/s
   * - MARS SYSTEM
     - | 110.6 h
       | (4.6 days)
       | Δv 781.4 km/s
     - | 
       | 〰
       | 
     - | 170.8 h
       | (7.1 days)
       | Δv 1.2 Mm/s
     - | 
       | 
       | 
     - | 
       | 
       | 
   * - ASTEROID BELT
     - | 
       | 
       | 
     - | 
       | 
       | 
     - | 
       | 〰
       | 
     - | 
       | 
       | 
     - | 
       | 
       | 
   * - JOVIAN SYSTEM
     - | 
       | 
       | 
     - | 
       | 
       | 
     - | 
       | 
       | 
     - | 
       | 〰
       | 
     - | 
       | 
       | 
   * - SATURNIAN SYSTEM
     - | 
       | 
       | 
     - | 
       | 
       | 
     - | 
       | 
       | 
     - | 
       | 
       | 
     - | 
       | 〰
       | 

