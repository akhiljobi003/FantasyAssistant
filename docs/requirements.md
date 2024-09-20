## 1. Team Info and Policies 
### Team Members and Roles 
* Lily Stauffer – Product Owner 
* Yohanse Nurga  - Scrum Master 
* Akhil Jobi – Database Manager 
* Mahir Sadique – Frontend Developer  
* Syed - Backend Developer
### Relevant Artifacts
* [Lasagnah/FantasyAssistant · GitHub](https://github.com/Lasagnah/FantasyAssistant) 
### Communication Channels 
* FantasyAssistant Discord Channel 
## 2. Product Description 
### Major Features: 
* Team creation/drafting simulation 
* Outcome prediction 
* LLM to help during drafting 
* Generation of visualizations 
### Stretch Goals: 
* Models to apply to multiple sports 
* Increasing model accuracy 
## 3. Use Cases 
### Use Case: Draft Team in Fantasy Sports 
* Goal In Context: Enable a user to draft an optimal team for their fantasy sports league using AI-assisted recommendations.  
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal 
* Preconditions 
    * User has access to AI systems.  
    * League settings and scoring rules are configured. 
    * Draft has been initiated.  
* Success End Condition: User has successfully drafted a complete team that adheres to league rules and maximizes potential points based on AI recommendations. 
* Failed End Condition: Draft is incomplete, team violates league rules, or user is unsatisfied with the drafted team. 
* Primary Actor: Fantasy Sports Player 
* Trigger: User initiates the draft process or responds to their turn in an ongoing draft.  
* Main Success Scenario: 
1. System presents current draft state and available players. 
2. System analyzes league scoring rules, remaining players, and team needs. 
3. System generates and presents top recommendations for the next draft pick. 
4. User reviews recommendations and player statistics. 
5. User selects a player to draft. 
6. System confirms the selection and updates the user's team roster. 
7. Steps 1-6 repeat until the user's team is complete. 
Extensions:  
* 2a. Unable to analyze league rules or player data: 
    * System notifies user of the issue. 
    * System provides option to proceed with limited functionality or contact support. 
* 3a. No suitable recommendations available: 
    * System informs user and suggests broadening search criteria. 
* 5a. User disagrees with recommendations: 
    * User requests alternative recommendations. 
    * System generates new recommendations based on adjusted criteria. 
    * Return to step 4. 
* 5b. User's preferred player is already drafted: 
    * System alerts user and suggests alternatives. 
    * Return to step 4. 
* 6a. Selected player violates league rules (e.g., salary cap, roster limits): 
    * System warns user of the violation. 
    * System suggests alternatives that comply with rules. 
    * Return to step 4. 
### Use Case: Trading Players in Fantasy Sports 
* Goal In Context: Enable a user to swap players for another player.  
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal 
* Preconditions 
    * User has access to AI system 
    * Draft has been initiated or completed.  
* Success End Condition: User has successfully completed a trade of players or swapped a player.  
* Failed End Condition: User is unable to swap a player onto their team for some reason (e.g., other player denies trade offer, player unavailable) 
* Primary Actor: Fantasy Sports Player 
* Trigger: User attempts to initiate a trade.  
* Main Success Scenario:  
1. System presents current draft state and available players. 
2. User attempts to create a trade offer.  
3. User 2 accepts or denies trade offer.  
4. If User 2 accepts the trade offer, swap the desired players.  
5. If User 2 denies the trade offer, close the trade offer.  
* Extensions: 
* 2a. Selected players violate league rules (e.g., salary cap, roster limits): 
    * System warns user of the violation. 
    * System suggests alternatives that comply with rules. 
    * Return to step 1.  
### Use Case: Waiver Wire Analysis 
* Goal In Context: Enables users to pick up the best available players and drop a player from your team 
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal 
* Preconditions:   
    * The players to be picked up is available in the waiver wire  
    * The user has an available roster spot or a player they are willing to drop 
* Succes End Condition: The user was successfully able to pick up a player from the waiver wire  
* Failed End Conditions: The user wasn't able to pick up the player they put in claim from the waiver wire  
* Primary Actor: Fantasy Sports player  
* Trigger: User puts in a claim for a player in the waiver wire  
* Main Succes Scenario:  
1. System shows the user what players are available in the waiver wire  
2. The user decides what player they want from the waiver wire and what player they want to drop from the roster  
3. The user adds the player or put the claim in the for the player, and click the drop button from roster they want to drop  
4. The system asks for the confirmation for the selections that they choose, and they update the roster  
* Extensions:  
    * The selected player is no longer available in the waiver wire list because it was picked by another team  
    * The users team roster is full and they don't want to drop any players from the roster 
### Use Case: Lineup Optimization 
* Goal In Context: Enables user to put the best lineup each week 
* Scope: Fantasy Basketball Assistant System 
* Level: User Goal 
* Precondition:  
    * Users team and player stats are loaded into the analyzer 
    * League scoring system must be understood by the analyzer 
* Success End Condition: User has updated lineup to the best potential based on projections and Analyzer suggestions 
* Failed End Condition: Analyzer receives outdated, or wrong player data and user does not create the best possible lineup 
* Primary Actor: Fantasy Sports Player 
* Trigger: The user requests lineup optimization to maximize their team’s performance based on current player statuses, matchups, or recent performance. 
* Main Success Scenario: 
1. User provides analyzer with current roster, league scoring rules 
2. Analyzer collects stats and league scoring rules and player performance, matchup and other factor that might impact the player 
3. Apply algorithm to suggest best possible lineup, selecting players who projects the most points 
4. Present lineup to user and provide rationale behind the recommendations 
5. User can review recommendations and make necessary adjustments 
* Extensions: 
    * Analyzer can handle changes to lineup such as injuries, trades or other mid season adjustments 
    * Incorporate user preferences for specific players 
    * Provide new recommendations in response to new information or last-minute injury reports 
### Use Case: Injury Management 
* Goal In Context: Enable players to be substituted when they are injured 
* Scope: Fantasy Sports Draft Assistant System 
* Level: User Goal  
* Preconditions: 
    * System notifies user that their is an injured player in the starting lineup 
    * User picks and substitutes a player from available bench players 
* Success End Condition: User substituted an injured player successfully  
* Failed End Condition: substituted player might not be the best in statistical stand point, compared to the injured player 
* Primary Actor: Fantasy Sports Player 
* Trigger: Lineup player injury 
* Main Success Scenario: If the substitute has same level of stat with the injured player 
## 4. Non-Functional Requirements 
* Every year/season that goes by, our model and program would have to be updated/trained again. 
* System should be available 24/7 and be able to provide responses quickly 
* UI should be user friendly allowing users to manage and utilize features  
## 5. External Requirements 
* When drafting, a user may attempt to draft a player by inputting their name in the “FirstName, LastName” format.  
* When drafting, a user may attempt to trade a player by inputting “trade Player1 Player2”. 
* If a user’s input does not match any of the previous inputs, then the user will be notified, and they will continue drafting.  
* The product should be a basic python script with a few extra files/folders attached to make it easily runnable.  
## 6. Team Process Description  
### Tools
* Tools we are going to be using includes Python, Pytorch, LLM packages, and Data Science packages, as well as PostgreSQL for our database. 
    * We will be using Python because it is the easiest programming language for what we are trying to accomplish. 
    * We will be using Pytorch, LLM packages, and Data Science packages to make it easier to implement the things they are associated with, so that we don't have to create the things from scratch. 
    * We will be using PostgreSQL for our database because its easy and open source. It's starting to become an industry standard. 
### Team member roles
* Lily's role is the Product Owner, her job is to help define what goes into the product. She also is helping with development where she can. She chose this role because she was the one to pitch this product, so she already had a view for what the product would be. The team needs this role filled to have a solid way forward and a solid list of goals for development. 
* Yohanse's role is the Scrummaster, his job is to help the developers be able to do what they need to do. 
* Akhil's role is the Database Manager, his job is to create and manage the database and datasystems.
* Mahir's role is the Frontend developer, his job is to create the way that the user interacts with our program.
* Syed's role is the Backend developer, his job is to create the way that our program responds to the input from the user. 
### Schedule
* Developer's Schedule
    * Create system infrastructure by October 4th.
    * Create system database by October 4th. 
    * Train system by October 25th.
    * Create LLM by November 29th.
    * Process external feedback December 6th.
### Risks
* The biggest risk has to do with our data. If we don't have a good dataset or way of storing our data, our product just can't really work well or in some cases even at all. 
* Another potential risk has to do with 
### External Feedback
* We will be processing external feedback the week of December 6th, which is basically after we have most of our product finished. We do this then because at that point, we have everything set up and we are able to easily incorporate feedback that doesnt fundamentally change how our program works. We would incorporate things that would potentially require us to retrain our models, but that would probably be the most significant. 