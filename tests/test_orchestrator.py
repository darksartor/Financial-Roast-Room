from financial_roast_room.agents import DeterministicAgent
from financial_roast_room.models import Criterion, InvestmentOption, Session
from financial_roast_room.orchestrator import RoastRoom


def test_valid_session_returns_synthesis():
    session = Session(
        question="Choisir une option",
        context="Simulation",
        horizon="5 ans",
        criteria=[Criterion("risque", 0.6), Criterion("liquidité", 0.4)],
        options=[InvestmentOption("A", "Option A")],
    )
    room = RoastRoom(session, [DeterministicAgent("Agent 1")])

    result = room.run()

    assert result["stage"] == "synthesis"
    assert len(result["decisions"] == 1 if False else result["decisions"]) == 1
    assert result["disclaimer"]


def test_weights_must_sum_to_one():
    session = Session(
        question="Choisir",
        context="",
        horizon="",
        criteria=[Criterion("risque", 0.7), Criterion("liquidité", 0.4)],
        options=[InvestmentOption("A", "Option A")],
    )

    try:
        RoastRoom(session, [DeterministicAgent("Agent")])
    except ValueError as error:
        assert "pondérations" in str(error)
    else:
        raise AssertionError("Une pondération invalide aurait dû être rejetée")
