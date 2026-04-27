# Guess the Random Number Game

This project is a CLI-based "Guess the Random Number" game. It challenges the player to identify a hidden number within a specified range, providing hints (higher/lower) and managing limited attempts based on the selected difficulty. The project tracks my evolution as a developer, moving from basic script-writing to implementing robust input validation, dynamic user interaction, and clean game lifecycle management.

---

## Features

* **Customizable Ranges:** Option to define game boundaries or use a default 1-20 range.
* **Difficulty Settings:** Choice between "Easy" (10 attempts) and "Hard" (3 attempts).
* **Robust Input Validation:** Uses `try-except` blocks to handle non-numeric inputs without crashing.
* **Dynamic Feedback:** Employs randomized message banks to provide a unique and engaging experience during every session.
* **Graceful Lifecycle:** Clean game exit and clear status updates upon winning or losing.

---

## Versions

| Version | Focus | Key Improvement |
| :--- | :--- | :--- |
| **V1** | Foundations | Simple `while` loop with basic guess logic. |
| **V2** | Game State | Added difficulty levels and life/chance tracking. |
| **V3** | Flexibility | Implemented user-defined ranges with boundary safety. |
| **V4** | Polish | Full error handling, random UI messaging, and lifecycle management. |

---

## What I Learned

Throughout this development process, I transitioned from basic logical flow to writing professional-grade code:  
* Mastered `try-except` blocks to maintain game stability against invalid user inputs.
* Learned to control game flow effectively using conditional logic and `break` statements.
* **User Experience (UX):** Discovered the power of `random.choice()` and list-based messaging to create dynamic, non-robotic interaction.
* Implemented functions like `min()` and `max()` to prevent errors when users input ranges in the wrong order.

---

## Note

While I have included all versions to showcase my progression, **Version 4** is the final, most robust, and recommended version for the best playing experience.

---

## Date
27 April 2026
