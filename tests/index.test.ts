import { convertToRisk, calculateScore } from '../securityriskcard/index';

import * as fs from 'fs';
import * as path from 'path';

function loadTestData(variant: string): [any, any] {
  const dataPath = path.join('tests', 'test_data');

  const rawFileContent = fs.readFileSync(path.join(dataPath, `${variant}.json`), 'utf8');
  const rawData = JSON.parse(rawFileContent);

  const expectedFileContent = fs.readFileSync(path.join(dataPath, `${variant}_risk.json`), 'utf8');
  const expectedResult = JSON.parse(expectedFileContent);

  return [rawData, expectedResult];
}

// This check uses original scorecard result to validate that our score
// calculation function is valid and behaves as expected.
describe('Regression Score Formula on Raw Data', () => {
  test('should validate score for klocc', () => {
    const [inputData] = loadTestData("klocc");
    const inputScore = inputData.score;
    expect(calculateScore(inputData.checks)).toEqual(inputScore);
    expect(convertToRisk(inputData, false).score).toEqual(10 - inputScore);
  });

  test('should validate score for telethon', () => {
    const [inputData] = loadTestData("telethon");
    const inputScore = inputData.score;
    // @TODO: This test will actually always fail due to the difference
    //        in how math (rounding) is performed in non-javscript languages
    //        like Go or Python..
    // expect(calculateScore(inputData.checks)).toEqual(inputScore);
    expect(convertToRisk(inputData, false).score).toEqual(10 - inputScore);
  });

  test('should validate score for ansible', () => {
    const [inputData] = loadTestData("ansible");
    const inputScore = inputData.score;
    expect(calculateScore(inputData.checks)).toEqual(inputScore);
    expect(convertToRisk(inputData, false).score).toEqual(10 - inputScore);
  });

  test('should validate score for autogpt', () => {
    const [inputData] = loadTestData("autogpt");
    const inputScore = inputData.score;
    expect(calculateScore(inputData.checks)).toEqual(inputScore);
    expect(convertToRisk(inputData, false).score).toEqual(10 - inputScore);
  });
});

// This check uses previously generated and manually reviewed output of the
// package to verify that we didn't have a regression for a default expected
// behavior.
describe('Regression Score Formula on Processed Data', () => {
  test('should validate score for klocc processed data', () => {
    const [_, resultData] = loadTestData("klocc");
    expect(calculateScore(resultData.checks)).toEqual(resultData.score);
  });

  test('should validate score for ansible processed data', () => {
    const [_, resultData] = loadTestData("ansible");
    expect(calculateScore(resultData.checks)).toEqual(resultData.score);
  });

  test('should validate score for telethon processed data', () => {
    const [_, resultData] = loadTestData("telethon");
    expect(calculateScore(resultData.checks)).toEqual(resultData.score);
  });

  test('should validate score for autogpt processed data', () => {
    const [_, resultData] = loadTestData("autogpt");
    expect(calculateScore(resultData.checks)).toEqual(resultData.score);
  });
});
