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

Emergency Breaks and Abrupt Trajectory Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is undesired, but not extremely rare, to have to abort a planned brachistochrone transit (full or partial) for some reason. Maybe there is an unexpected object in a collision course; perhaps there’s an emergency that requires “stopping” (or considerably slowing down); maybe there is a distress call nearby that needs attention or immediate action; perhaps the captain decides to change destination mid-flight. Whatever the case, a vessel that is darting through space (either in a 0G drift or under thrust) will need to accrue an unexpected Δv cost to reduce speed.

In order to **execute a maneuver to come to a full stop while in transit** (either full thrust or partial drift), follow these steps:

1. Take note of the original Δv cost of the trip (Δvₒ) that was still not fully spent.
2. Find out how much time has passed in transit in hours (Aₜ), and compare with the original total time for the trip (Tₜ). Calculate this percentage with this formula:

.. math::

    P_t = \frac{A_t-T_t}{/T_t} * 100

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

Interplanetary Transits
~~~~~~~~~~~~~~~~~~~~~~~

0.01G of Acceleration
^^^^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 0.01G:

.. figure:: /_static/images/sci-fi-travel-time-0-01G.jpg

0.1G of Acceleration
^^^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 0.1G:

.. figure:: /_static/images/sci-fi-travel-time-0-1G.jpg

0.2G of Acceleration
^^^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 0.2G:

.. figure:: /_static/images/sci-fi-travel-time-0-2G.jpg

0.3G of Acceleration
^^^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 0.3G:

.. figure:: /_static/images/sci-fi-travel-time-0-3G.jpg

0.4G of Acceleration
^^^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 0.4G:

.. figure:: /_static/images/sci-fi-travel-time-0-4G.jpg

0.5G of Acceleration
^^^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 0.5G:

.. figure:: /_static/images/sci-fi-travel-time-0-5G.jpg

1G of Acceleration
^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 1G:

.. figure:: /_static/images/sci-fi-travel-time-1G.jpg

2G of Acceleration
^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 2G:

.. figure:: /_static/images/sci-fi-travel-time-2G.jpg

3G of Acceleration
^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 3G:

.. figure:: /_static/images/sci-fi-travel-time-3G.jpg

5G of Acceleration
^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 5G:

.. figure:: /_static/images/sci-fi-travel-time-5G.jpg

10G of Acceleration
^^^^^^^^^^^^^^^^^^^

Average Travel Time and Δv Cost between planetary systems at 10G:

.. figure:: /_static/images/sci-fi-travel-time-10G.jpg

Inter-System Transits
~~~~~~~~~~~~~~~~~~~~~

Average Travel Time and Δv Cost between Stations, Moons and Satellite Lagrangian Points in the same planetary system [#]_:

.. [#] For objects at distances approximate to moon orbits or planet-moon Lagrangian Points. The average distance from Earth to Luna (384400 km) was used to calculate these values. L4 and L5 are roughly at the same distance (326400 km) which makes it close enough that you can use this same table.

.. figure:: /_static/images/sci-fi-travel-time-intersystem.jpg

.. figure:: /_static/images/earth-moon-lagrange-points.png

   This image shows Earth-Luna Lagrangian Points. The distance to Earth-Sun Lagrangian Points is much vaster (L4 and L5 are 30 million km away from Earth), that they are not considered Inter-system Transits. You can calculate transit times and costs manually to these points if needed. 

Inter-Orbit Transits
~~~~~~~~~~~~~~~~~~~~

Average Travel Time and Δv Cost between Stations in planetary orbit [#]_:

.. [#] For distances between objects in the orbit of a planet. The average distance of 30,000 km was used for these calculations. Since distances between low and high orbits are negligible for the purposes of Δv budget costs, you can use this same table for any.

.. figure:: /_static/images/sci-fi-travel-time-interorbit.jpg