methods {
    normalizedWeight1() returns uint256 envfree
    normalizedWeight2() returns uint256 envfree
}
rule updateOracleShouldNotRevert(uint256 lastChangeBlock,
    uint256 balanceToken0,
    uint256 balanceToken1) {
    env e;

    require e.msg.value == 0;
    require normalizedWeight1() > 0;
    require normalizedWeight2() > 0;
    require balanceToken0 > 0;
    require balanceToken1 > 0;

    updateOracle@withrevert(e, lastChangeBlock, balanceToken0, balanceToken1);
    bool success = !lastReverted;
    assert success, "updateOracle reverted";
}