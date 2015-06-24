df1 = pd.DataFrame(np.random.randn(6,3), columns=['A', 'B', 'C'])

df2 = pd.DataFrame(np.random.randn(6,3), columns=['D','E','F'])

df = pd.concat([df1, df2], axis=1)

df
