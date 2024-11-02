# Modelowanie Kształtu Jajka w OpenGL

Ten projekt modeluje kształt jajka w trójwymiarze przy użyciu wielomianowej parametryzacji. Model został zrealizowany za pomocą funkcji OpenGL i prymitywu `GL_LINES`, aby przedstawić owalny kształt jajka. Projekt wykorzystuje język Python z biblioteką `PyOpenGL` oraz `GLFW` do obsługi okna graficznego.

---

### Opis Modelu

Kształt jajka został odwzorowany poprzez odpowiednią kombinację wielomianów piątego stopnia dla współrzędnych `x`, `y` i `z`. Używając parametrów `u` i `v`, można uzyskać gładką, owalną formę o symetrii pionowej. Parametry te definiują odpowiednio profil i szerokość jajka.

### Teoria Parametryzacji Kształtu Jajka

Model jajka bazuje na wielomianie piątego stopnia. Każda z współrzędnych jest funkcją parametrów:
- `u` określa wysokość jajka, przebiegając od 0 (dół) do 1 (góra).
- `v` definiuje szerokość wokół osi symetrii, obracając się o `2π`.

Przy odpowiednich wartościach współczynników wielomianów stopnia piątego, otrzymujemy profil kształtu, który zwęża się przy jednym końcu i zaokrągla na drugim, przypominając jajko.

### Wzory Matematyczne

1. **Współrzędne `x` i `z`** - odpowiadają za szerokość jajka, tworząc profil eliptyczny:

   - `x(u, v) = f(u) * cos(π * v)`
   - `z(u, v) = f(u) * sin(π * v)`

   gdzie:
   
   - `f(u) = -90 * u^5 + 225 * u^4 - 270 * u^3 + 180 * u^2 - 45 * u`

   Funkcja `f(u)` wyznacza eliptyczny profil w płaszczyźnie poziomej.

2. **Współrzędna `y`** - odpowiada za profil pionowy:

   - `y(u) = 160 * u^4 - 320 * u^3 + 160 * u^2 - 5`

   gdzie `y` tworzy charakterystyczne spłaszczenie u dołu oraz zaokrąglenie u góry.

Wartości współczynników `-90`, `225`, `-270`, `180`, i `45` zostały dobrane eksperymentalnie, aby uzyskać naturalny, owalny kształt.

### jajko z lini

    glBegin(GL_LINES)
    for i in range(N - 1):
        for j in range(N - 1):
            # Połączenie (i, j) z (i + 1, j)
            glVertex3f(*tab[i, j])
            glVertex3f(*tab[i + 1, j])

            # Połączenie (i, j) z (i, j + 1)
            glVertex3f(*tab[i, j])
            glVertex3f(*tab[i, j + 1])

    glEnd()


### jajko przy pomocy trójkątów

    glBegin(GL_TRIANGLES)
    for i in range(N - 1):
        for j in range(N - 1):
            glVertex3f(*tab[i,j+1])
            glVertex3f(*tab[i, j])
            glVertex3f(*tab[i + 1, j])
            
            glVertex3f(*tab[i, j + 1])
            glVertex3f(*tab[i+1, j+1])
            glVertex3f(*tab[i + 1, j])
    glEnd()


### jajko za pomocą GL_TRIANGLE_STRIP

    for i in range(N - 1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(N):
            glColor3f(*colors[i][j])  # Kolor dla wierzchołka
            glVertex3f(*tab[i, j])  # Wierzchołek dla wiersza i
            glColor3f(*colors[i + 1][j])  # Kolor dla wierzchołka
            glVertex3f(*tab[i + 1, j])  # Wierzchołek dla wiersza i + 1
        glEnd()
    glFlush()

### Wyjaśnienie

1. **Iteracja przez wiersze**: Zewnętrzna pętla `for i in range(N - 1)` iteruje przez wiersze, a wewnętrzna pętla iteruje przez kolumny, aby dodać wierzchołki do `GL_TRIANGLE_STRIP`.

2. **Dodawanie wierzchołków**: W każdej iteracji dodawany jest wierzchołek z wiersza `i`, a następnie wierzchołek z wiersza `i + 1`. Dzięki temu każdy dodany wierzchołek łączy się z dwoma wcześniejszymi, co tworzy pasy trójkątów.

3. **Ograniczenie do N-1**: Pętla zewnętrzna ogranicza się do `N - 1`, aby uniknąć przekroczenia indeksów, ponieważ `tab` ma rozmiar `N x N`.

### Korzyści z użycia `GL_TRIANGLE_STRIP`

Zastosowanie `GL_TRIANGLE_STRIP` zwiększa efektywność renderowania, ponieważ pozwala na ponowne wykorzystanie wierzchołków i zmniejsza liczbę wywołań do GPU, co przekłada się na lepszą wydajność aplikacji graficznych.
