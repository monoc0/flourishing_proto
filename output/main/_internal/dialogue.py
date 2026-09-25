class question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

q_test = question("a or b", ["a", "b"])

q_i="""
Leo is a student, he is just trying his best to go through school.
Recess had begun and he decided to go to the nearby store, which has a decent stretch of non-school ground through the journey.
He then bought some bread and other groceries. As he passes by, he caught a glimpse of a homeless man curled up in a dark corner
"""
q_1=question("What will Leo do?", ["Help out the homeless man by giving him food.","Ignore and move on."])
q_1a="""
Thinking for a while, with the bread and its cost, Leo reluctantly gave the homeless man food.
He thought a lot about what the bread would've tasted like, but had a feeling this was the right decision as the homeless man thanked him.
"""
q_1b="""
Thinking for a bit, Leo had thought of giving the homeless man his bread, but thought about its cost and decided not to.
He then immediately walked faster, in hopes that the homeless man does not notice him.
"""
q_i2="""
Suddenly, some of his classmates saw him from a distance.
These classmates were quite mean in their manner of speaking, luckily they weren't in the mood to target Leo that day. Leo despised them, despite not being a previous victim yet.
Walking past, he tripped on a rock and then he heard laughing from a distance. It was those classmates, they saw him and couldn't hold back their laughter.
"""
q_2=question("What should Leo do?", ["Insult the classmates in retaliation.","Ignore and don't take it personally."])
q_2a="""
Leo shouted an insult out loud and started running away.
He had a sense of regret that immediately overshadowed him.
"""
q_2b="""
With a heavy heart, Leo got up and ignored the laughter.
Its not worth taking personally anyways.
"""
q_i3="""
After getting past the rude classmates, he saw a friend looking down at the floor, traumatized by the floods in her area.
Leo noticed immediately, but knew that if he walked past, she wouldn't notice him.
"""
q_3=question("What should Leo do?", ["Ignore her and look at your phone.","Talk and ask what's up."])
q_3a="""
Leo walked past and looked at his phone to then check some messages, which he only left on read."""
q_3b="""
Leo walked towards his friend and started a conversation.
After the conversation, the bond between Leo and his friend has strengthened.
"""
q_i4="""
Leo then remembered that he had bought chips.
He thought about eating it, even though his original intention was to give it to his siblings.
"""
q_4=question("What should Leo do?", ["Stick to the plan.","Devour the chips."])
q_4a="""
Hesitantly, he resisted eating the chips.
He wanted it very badly, but felt like sticking to the plan felt like the right thing to do.
"""
q_4b="""
He opened the chips and immediately plunged his hand inside.
30 seconds later, the bag of chips is empty.
"""
q_i5="""
Walking back to the classroom, Leo remembered the quiz in the next subject.
Now he only has 5 minutes left to review.
A thought crossed his mind to cheat in the exam.
"""
q_5=question("What should Leo do?", ["Wing the exam.","Devise a plan to cheat."])
q_5a="""
Leo decided to merely wing the exam.
...
After taking the exam, Leo felt a bit dreadful as he didn't know the answer to some questions. But despite that, Leo thought he did the right thing, and that he will take his grade with grace.
"""
q_5b="""
Leo devises a plan to cheat at the exam with his friends. After a bit of planning, the plan is a simple pen-tap signal, where the smart friend taps with correlation to the answers in the exam.
Unfortunately, the exam was mostly identification, so he just looked at his seatmate’s answers strategically instead.
The exam has ended and Leo has got off scot-free. Yet, he felt like he did something terrible, like an action he couldn’t take back.
"""
e_0="""
After all of that, Leo went through school as usual. He then went home and decided to reflect on his actions."""
e_1="""GOOD ENDING: Leo felt quite good for what he did today. He did actions that improved himself and his control over himself.
The END!"""
e_2="""NEUTRAL ENDING: Leo felt decent about his actions today, yet he felt like he could have made some decisions differently.
The END!"""
e_3="""BAD ENDING: Leo felt a bit regretful today, knowing how he couldn’t control some of his actions.
The END!"""