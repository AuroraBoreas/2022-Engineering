## Methods Of Geometry

my purpose is to find a better technics to solve geometry problems in engineering field;

learning by doing

- what: geometry
- why: understand geometry deeply and smartly
- how: methods
- note: @ZL, 20220718

### Mathematic Symbols

```
parallel //
perpendicular ⊥
union ∪
intersect ∩
triangle ∆ 
angle  ∠
degree °
congruent ≅ 
neq ≠
plusminus ±
minusplus ∓
```

### Content

1.intro
2.foundations
3.elementary euclidean geometry
4.exercises
5.triangle and circle geometry
6.plane isometries and similarities
7.three dimensional isometries and similaries
8.symmetry

### Sense

- geometry is everywhere!
- math is a sense

### Concepts

数拓多限转，构双椭投同

```
- AMS mathematics subject classification
- algebraic and differential geometry: topology
- convex incidence geometry and ordered geometries: finite geometry
- matric geometry and transformational geometry
- geometric constructions
- extremum problems
- hyperbolic and elliptic non-Euclidean geometries
- projective geometry and homogeneous coordinates
- computational geometry
```

## Chapter 2 Foundations

### 2.1 Geometry as applied mathematics

applied mathematics is characterized by its use of models.

- Mathematical modeling ("SMT")
- An example in astronomy
- Testing for accuracy, not correctness
- Testing a geometric model
- Conventionalism

![SMT]("./static/2.1.1_mathematical_modeling.png")

### 2.2 Need for rigor

concepts

```
- How much rigor is necessary?
- A sophism
- analysis: assumptions weren't checked; the diagram is wrong
- Opposite sides of a line
- Inside and outside of a segment or triangle
- Need for rigorous proofs
```

### 2.3 The Axiomatic Method

Concepts

```
- undefined concepts and definitions
- unproved axioms and proved theorems
- euclidean geometry
- the declaration of independence
- controversy over the role of undefined concepts
```

### 2.4 Euclid's Elements

concepts

```
- Evolution and influence of the Elements
- Its lack of undefined notions
- Euclid's axioms
- Their insufficiency
- Straightedge and compass constructions
- Incommensurable segments
- Hilbert's and Birkhoff's rigorous foundations
- What was the subject matter of the Elements?
```

Aristotle's guidenlines:

- point
- line
- length
- angle equality

Elements purports

Euclid postulates only five axioms of line segment:

```
1. to draw a straight line from any point to any point
2. to produce a finite straight line continuously in a straight line
3. to describe a circle with any centre and distance
4. that all right angles are equal to one another
5. that, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two stright lines, if produced indefinitely, meet on that side on which are the angles less than the two right angles.
```

### 2.5 Coordinate geometry

concepts

```
- Thinkings about numbers, independently of the object they measure
- Development of decimal arithmetic and algebra
- Solving cubic and quartic equations
- Negative numbers
- Descartes and coordinate geometry
```

### 2.6 Foundation problem

concepts

```
1. Are the Euclidean and coordinate models equivalent?
2. What are numbers?
3. Is every number the length of some segment?
4. Defining the real number system
5. Replacing and augmenting Euclid's axioms
```

### 2.7 Parallel axiom

concepts

```
- The parallel axiom is more complicated than the others
- Mathematicians tried to prove it as a theorem, but failed
- Is it independent of the other axioms?
- An answer requires a complete list of Euclid's unstated assumptions
- That's equivalent to the foundation problem
- Hilbert finally established the independence in 1899
- But non-Euclidean geometry had strongly suggested it much earlier
```

### 2.8 Firm foundations

concepts

```
- What must a firm foundation provide?
- Hilbert and the Italian school
- Geometric construction of real numbers
- Can a rigorous foundation be used for teaching?
- Birkhoff, School Mathmatics Study Group(SMSC), and chapter 3
```

### 2.9 Geometry as pure mathematics

concepts

```
- The axiomatic method in foundations of geometry
- Confusion over definitions
- Pieri's and Hilbert's use and views of undefined concepts
- Hilbert's dispute with Prege
- Implicit definitions
- The 1900 congresses and Padoa's paper
- Pure, abstract mathematics
- Russell's reaction
- Huntington's axiomatization of the real number system
- Modularization of mathematics
```

### Exercises and projects

concepts

```
- Scholarship skills
- Decimal arithmetic
- Algebra
- Paradigmatic shift and cultural evolution
```

## Chapter 3 Elementary Euclidean geometry

undefined concepts

```
3.1 point, line, plane
3.2 distance
3.4 angle measure
3.8 area
3.10 volume
```

axioms

```
3.1 incident axioms
3.2 ruler axiom
3.3 Pasch's axiom
3.4 protractor axioms
3.5 congruence axiom
3.7 parallel axiom
3.8 area axioms
3.10 volume axioms
```

### 3.1 Incidence geometry

concepts

```
- Points, lines, planes
- Incidence
- Collinearity, coplanarity, and concurrence
- Incidence axioms
- Incidence geometry
```

#### farther understanding
Lines and planes are regarded as *point sets* -- subsets of the set of all points, which is called space;

```
symbols
- letters A to Z are used to denote points;
- g to l for lines;
- α to ε for planes;

- in, on and through describe the membership;
- subset relations ⊆ and ∈ among points and point sets;
```

how to interpret?

you can *assemble* the corresponding images into figures that will be invaluable for steering you through the theory of this chapter.

but the intuitive representation will *never* be used essentially in the logical development of geometry. that will be based solely on the axioms.

```
incidence axioms I1 to I5.

Axiom I1: Any two distinct points O and P lie on a unique line OP. Each line passes through at least two distinct points;

Axiom I2: Any three noncollinear points O, P and Q lie in a unique plane OPQ. Each plane passes through at least three noncollinear point;

Axiom I3: If two distinct points O and P lie in a plane ε, then the line OP lies entirely in ε;

Axiom I4: If two plances pass through a point O, then they pass through another point P ≠ O;

Axiom I5: There exist noncoplanar points O, P, Q, and R such that O, P, and Q are noncollinear and O ≠ P;
```

it's convenient to organize the first part of the proof as lemma:

an auxiliary theorem not particularly interesting in itself.

```
Theorem 1. The intersection of two distinct intersecting lines is a point.
the intersection of a line and an intersecting but nonincident plane is a point.
the intersection of two distinct intersecting planes is a line;

Theorem 2. Through a point and a nonincident line passes a unique plane.
Through two distinct intersecting lines passes a unique plane;

Lemma 3. Points O and R of axiom I5 are distinct, and no three are collinear;

Theorem 4. Through any point S pass at least three noncoplanar lines and thre distinct planes. Through any line g pass at least two distinct planes;

```

### 3.2 Ruler axiom and its consequences

concepts

```
- Distance
- Scale and coordinates on a line
- Ruler axiom and ruler placement theorem
- Betweenness
- Segments and rays
- Convex sets
```

axiom

```
Ruler axiom. Each line has a scale;
Theorem 1. PQ = QP for all points P and Q. Moreover, PQ = 0 if and only if P = Q;

Theorem 2. Let c and d be scales for a line g through points X, Y and Z.
if c(Y) lies between c(X) and c(Z), then d(Y) lies between d(X) and d(Z).

Theorem 3 (Ruler placement theorem). Let O and P be distinct points. Then there's a unique scale c for OP such that c(O) = 0 and c(P) > 0.

Thm 4. Two rays OP and NQ are equal if and only if N = O and O-P-Q or O-Q-P. If Q-O-P, the line OP consists of O and the two opposite rays OP and OQ;

```

convex

```
a point set is called convex if it includes segment XZ whenever it contains X and Z;
```

![convex sets]("./static/3.2.2_convex_sets.png")

### 3.3 Pasch's axiom and the separation theorems

concepts

```
Triangle, vertices and edges
Pasch's axiom
Line, plane, and space separation theorems
Sides of a point in a line, of a line in a plane, and of a plane
```

Pasch's axiom

```
if a line in the plane of a triangle contains an interior point of one edge, it must intersect another edge.

Thm 1. No line can contain points interior to all three edges of a triangle;

Thm 2 (line separation theorem). Let O be a point on a line g. Then g is the union of three disjoint convex sets: O itself and two opposite rays, called the sides of O in g. Two points X and Y on g lie on the same side of O in g if and only if segment XY doesn't contain O. If P and Q are points distinct from O such that P-O-Q, then OP and OQ are the side of O in g;

Thm 3 (plane separation theorem). Let g be a line in a plane ε. Then ε is the three disjont convex sets: g itself and two sides of g in ε. Two points X and Y in ε lie on the same side of g in if and only if segment XY doesn't intersect g. If P is any point in ε not on g, then the two sides of ε are the sets
{Q ∈ ε: PQ ∩ g = φ}, {Q ∈ ε: Q !∈ g & PQ ∩ g != φ}

Thm 4 (space separation theorem). Let ε be a plane. Then the set of all points is the union of three disjoint convex point sets: ε itself and its two sides. Two points X and Y lie on the same side of ε if and only if segment XY doesn't intersect ε. if P is any point not on ε, then the two sides of are the sets
{Q: PQ ∩ ε = φ}, {Q: Q !∈ ε & PQ ∩ ε != φ}
```


### 3.4 Angles and the protractor axioms

concepts

```
Angles
Interior of an angle and of a triangle
Crossbar theorem
Degree measure
Protractor axioms
Liear and vertical pairs of angles
```


Theorems

```
Thm 1. Consider a point O on a line g, a point P not on g, and let ε be the plane through g and P. Then the ray OP lies entirely on one side of g in ε.

An angle is a point set of the form

∠POQ = OP ∪ O ∪ OQ, where O, P and Q are noncollinear points; O is called its vertex.

Thm 2. The interior of ∠POQ is convex. All interior points of segment PQ lie in the interior of ∠POQ. if R is a point in the interior of ∠POQ, then the ray OR lies entirely in the interior of ∠POQ.

Thm 3. Suppose Q and R are points on the same side of a line OP in a plane ε. Then exactly one of the following conditions holds:

1. Q lies in the interior of ∠POR
2. OQ = OR
3. R lies in the interior of ∠POR

Thm 4. Let O be an interior point of edge SQ of ∆SPQ and let R be a point in plane SPQ on the same side of SQ as P. Then the ray OR intersects SP or PQ;

Thm 5 (Crossbar theorem). Let R be a point in the interior of ∠POQ. Then OR intersects PQ.
```


measurement

```
Axiom P1. Let O and P be distict points in a plane ε and 0 < x < 180. Then on each side of OP in ε there's a point Q such that m∠POQ = x°.

Axiom P2. If Q is a point in the interior of ∠POR, then m∠POQ + m∠QOR = m∠POR.

Thm 6. In axiom P1, if R is a point on the same side of OP in ε as Q and m∠POQ = m∠POR, then OQ = OR, otherwise m∠QOR = 0°.

Axiom P3. The sum of the measures of the angles of a linear pair is 180°.

Thm 7 (Vertical angle theorem). Angles of a verticale pair have the same measure.

```


### 3.5 Congruence

concepts

```
Congruent segments and angles
Congruent triangles
SAS congruence axiom
ASA, SSS, and SAA congruence theorems
There's no SSA congruence theorem!
Isosceles triangle theorem
Equilateral triangles, scalene triangles
Exterior angle theorem
Triangle inequality
Hinge theorem
```

Hilbert

```
SAS congruence axiom. Consider triangle ∆XYZ and ∆X'Y'Z'. If XY = X'Y', ∠Y ≅ ∠Y', and YZ = Y'Z', then ∆XYZ ≅ ∆X'Y'Z'.

Thm 1 (ASA congruence theorem). Consider triangles ∆XYZ and ∆X'Y'Z'. If ∠X ≅ ∠X', XY = X'Y', and ∠Y ≅ ∠Y', then ∆XYZ ≅ ∆X'Y'Z'.

Corollary 2(Isosceles triangle theorem). Two angles of a triangle are congruent if and only if the opposite edges are.

Thm 3 (SSS congruence theorem). Consider triangles ∆XYZ and ∆X'Y'Z'. If XY = X'Y', YZ = Y'Z', and ZX = Z'X', then ∆XYZ ≅ ∆X'Y'Z'.

Thm 4 (Exterior angle theorem). Consider triangles ∆XYZ and a point W != X such that W-X-Y. Then m∠Y, m∠Z < m∠WXZ.

Thm 5 (SAA congruence). Consider triangles ∆XYZ and ∆X'Y'Z'. If ∠X ≅ ∠X', XY = X'Y', and ZX ≅ Z'X', then ∆XYZ ≅ ∆X'Y'Z'.

Lemma 6. In ∆XYZ, YZ < XY if and only if m∠X < m∠Z.

Thm 7 (Triangle inequality). If points X, Y, and Z are not collinear, then XY + YZ > XZ.

Thm 8 (Hinge theorem). In ∆XYZ and ∆X'Y'Z', suppose XY = X'Y' and XZ = X'Z'. Then m∠X < m∠X' if and only if YZ < Y'Z'.

```


### 3.6 Perpendicularity

concepts

```
Right, acute, and abtuse angles
Perpendicular lines and planes
Feet of perpendiculars
Distance from a point to a line or a plane
Perpendicular bisectors
Dihedral angles
```


theorems

```
Thm 1. Let P be a point on a line g in a plane ε. Then there's a unique perpendicular to g in ε through P.

Thm 2. Let P be a point not on a line g. Then there's a unique perpendicular to g through P.

Thm 3. The foot of the perpendicular to a line g through a point P not on g is the unique point on g whose distance from P is minimum.

Lemma 4. Let P,Q and X,Y be pairs of distinct points. If PX = XQ, PY = YQ, then PZ = ZQ for every point Z on XY.

Thm 5. Let g, h and k be lines through a point O such that g ⊥ h, k and h != k. Let ε be the plane through h and k, and l be any line through O. The g ⊥ l if and only if l lies in ε.

Thm 6. If P is a point and g a line, then P lies in a unique plane perpendicular to g.

Thm 7 (Perpendicular bisector theorem). For any distinct points P and Q, the perpendicular bisector of PQ is the set of all points equidistant from P and Q.

Thm 8. Any two lines g and h perpendicular to a plane ε are coplanar.

Τhm 9. If P is a point and ε a plane, then P lies on a unique line g perpendicular to ε.

Thm 10. The foot of the perpendicular to a plane ε through a point P is the unique point in ε whose distance from P is minimun.

Thm 11 (Dihedral angle theorem). All angles belonging to dihedral angle δ' ∪ g ∪ ε' are congruent.

Thm 12. Let δ and ε be planes whose intersection is a line g. Let h be a line in δ perpendicular to g. Then h ⊥ ε if and only if δ ⊥ ε.

```

![Dihedral angle theorem]("./static/3.6.2_theorem11.png")


### 3.7 Parallel axiom and relate theorems

concepts

```
Absolute geometry
Parallel lines and planes, and the distance between them
Alternate interior angles
Parallel axiom -- Euclid's and Playfair's versions
Transitivity theorems for parallels
Sum of the measures of the angles of a triangle
Strong exterior angle theorem
Invariance of betweenness under parallel projection
Convex quadrilaterals: trapezoids, parallelograms, rhombi, rectangles, and squares
Right triangles, their hypotenuses and legs: 30°-60° right triangles
Oblique triangles
```


theorems

```
Thm 1 (alternative interior angles theorem, p1). Let O, P, Q, and R be points in a plane ε, as shown in figure 3.7.1, with O != P and with Q and R on different sides of OP. If ∠QOP ≅ ∠RPO, then OQ // PR.
```

![alternative interior angles theorem]("./static/3.7.1_alternative_interior_angles_theorem.png")


```
Corollary 2. Two coplanar perpendiculars to the same line are parallel. Two lines perpendicular to the same plane are parallel.

Corollary 3. If P is a point not on a line g, then there exists at least one parallel to g through P.

Parallel axiom. If P is a point not on a line g, then there exists at most one parallel to g through P.

Thm 4 (Euclid's parallel axiom). Let O, P, Q, and R be points in a plane ε with O != P and with Q and R on different sides of OP. If m∠QOP > m∠RPO, then OQ intersects PR on the same side of OP as R.

Thm 5 (Alternative interior angles theorem, p2). Let O be a point in a line g in a plane ε, let Q and R be points in ε on different sides of g, and let h be a line in ε through R. If OQ // h, then h intersects g at a point P != Q, and ∠POQ ≅ ∠OPR.

Corollary 6. Let g, h, and k be a coplanar liness such that g ⊥ h and h != k. Then h // k if and only if g ⊥ k.

Corollary 7. Let ε be a plane and h and k be lines such that h ⊥ ε and h != k. Then h // k if and only if k ⊥ ε.

Corollary 8 (Transitivity theorem for parallel lines). Let g, h, and k be distnct lines. if g // k and h // k, then g // h.

Corollary 9 (Triangle sum theorem). The sum of the measures of the angles of a triangle is 180°.

Corollary 10. An equilateral triangle has three 60° angles. An isosceles right triangle has two 45° angles.

Corollary 11 (Strong exterior angle theorem). Consider XYZ and a point W != X such that W-X-Y. then m∠WXZ = m∠Y + m∠Z.

Thm 12. Let g be a line, and δ and ε be distinct planes and g ⊥ δ. Then // if and only if g ⊥ ε.

Thm 13 (Transitivity theorem for parallel planes). Let α, β, and γ be distinct planes. if α // γ and β // γ, then α // β.

Thm 14 (Invariance of betweenness under parallel projection). Let parallel lines g, h, and j intersect a line k at points X, Y, and Z, and a line k' at points X', Y', Z'. If X-Y-Z, then X'-Y'-Z'.

Thm 15. The following conditions on a quadrilateral in a plane ε are equivalent:
1.each edge lies entirely on one side of the line in ε that includes the opposite edge;
2.each vertex lies in the interior of the opposite angle;
3.the diagonals intersect.

Thm 16. A trapezoid is a convex quadrilateral, hence its diagonals interset.

Thm 17. For any noncollinear points P, Q, and R, there's a unique point S such that PQRS is a parallelogram.

Thm 18 (Parallelogram theorem). The following conditions on a quadrilateral PQRS are equivalent:
1. PQRS is a parallelogram,
2. PQ = RS and QR = SP,
3. ∠P ≅ ∠R and ∠Q ≅ ∠S,
4. PQ // RS and PQ = RS,
5. the diagonals of PQRS intersect at their common midpoint.

Thm 19. The diagonals of a parallelogram lie in perpendicular lines if and only if it's a rhombus.

Thm 20. All angles of a rectangle are right. Any parallelogram with one right angle is a rectangle.

Thm 21. If g and h are parallel lines and P and P' are points in g, then the distances from P and P' to h are equal. Similar results hold for a parallel line and plane, and for parallel planes.

Thm 22. The midpoint of the hypotenuse of a right triangle is equidistant from vertices.

Thm 23. Consider ∆OPQ with right angle O. Then OP = 1/2 PQ if and only if m∠P = 60° and m∠Q = 30°.
```


### 3.8 Area and Pythagoras' theorem

concept

```
Triangular and polygonal regions
Interior and boundary points, edges, and vertices
Area axioms
Bases and altitudes of trapezoids and triangles
Areas of squares, rectangles, triangles, trapezoids, and parallelograms
Pythagoras' theorem
Existance of a triangle with given sides
Alternative area theories based on similarity or integration
```

Theorems

```
Thm 1. If point X, Y, and Z are noncollinear, then the following sets coincide:
1.the triangular region determined by ∆XYZ,
2.the union of the edges of ∆XYZ with the intersection of the interiors of any two of its angles,
3.the intersection of all convex point sets containing X, Y, and Z.

Thm 2. If PQRS is a convex quadrilateral, then the following point set coincide:
1.the union of the triangular regions determined by ∆PQR and ∆RSP,
2.the union of the triangular regions determined by ∆QRS and ∆SPQ,
3.the union of the edges of PQRS with the intersection of the interiors of any two opposite angles,
4.the intersection of all convex point sets containing P, Q, R, and S.

Thm 3. If PQRS is a nonconvex quadrilateral, then exactly one pair of opposite vertices line on opposite sides of the line through the other two.

Thm 4. The region determined by a quadrilateral PQRS is convex if and only if PQRS is a convex quadrilateral.

```

in general, a *polygonal region* is defined to be the union of a finite set of triangular regions, any two of which intersect, if at all, in a point or segment.

clearly, all triangular regions are polygonal regions; and the region determined by a quadrilateral is a polygonal region in the general sense.


```
Thm 5. If the intersection of polygonal regions Ε and T is empty or the union of a finite set of points and segments, then Ε ∪ Τ is a polygonal region.

Axiom A1. Regions determined by congruenct triangles have the same area.

Axiom A2. If the intersection of polygonal regions Ε and Τ is empty or the union of a finite set of points and segments, then a(Ε ∪ Τ) = aΕ + aΤ

Axiom A3. The area of a square is the square of one its edges.

Thm 6. The area of a rectangle is the product of a base b by the corresponding altitude a.

Corollary 7. The area of a right triangle is half the product of its legs.

Thm 8. If the foot of an altitude of a triangle falls outside the base, then the nearer base angle is obtuse. If both base angles are acute, the foot is on the base.

Thm 9. The area of a triangle is half the product of a base b by the corresponding altitude a.

Corollary 10. The area of a trapizoid is half the product of an altitude by the sum of the corresponding bases.

Corollary 11. The area of a parallelogram is the product of a base by the corresponding altitude.

Thm 12 (Pythagoras' theorem). The square of the hypotenuse of a right triangle is the sum of the squares of its legs.

Corollary 13. Distinct points O, P, and Q, such that (OP)^2 + (OQ)^2 = (PQ)^2, are noncollinear and form a right angle ∠POQ.

Thm 14. Let x, y, and z be positive real numbers, each of which is less than the sum of the other two. Then there is a triangle whose edges have lengths x, y, and z.
```


### 3.9 Similarity

concepts

```
Similar triangles
Similar ratio
Invariance of distance ratios under parallel projection
AA, SAS, and SSS similarity theorems
Ratio of areas of similar tiangles
Alternative proof of Pythagoras' theorem
```

Theorems

```
Thm 1 (Transitivity of similarity). If ∆XYZ ~ ∆X'Y'Z' and ∆X'Y'Z' ~ ∆X''Y''Z'', then ∆XYZ ~ ∆X''Y''Z'', and the ratio of the third similarity is the product of the ratios of the first two.


Thm 2. Let X' and Y' be distinct points on edges XZ and YZ of ∆XYZ. Then XY // X'Y' if and only if XX'/X'Z = YY'/Y'Z.

Corollary 3 (Invariance of distance ratios under parallel projection). Let parallel lines g, h, j intersect lines k and l at points X, Y, Z and X', Y', Z'. Then XY / YZ = X'Y'/Y'Z'.

Thm 4 (AA similarity theorem). Consider ∆XYZ and ∆X'Y'Z'. If ∠X ≅ ∠X' and ∠Y ≅ ∠Y', then ∆XYZ ~ ∆X'Y'Z'.

Thm 5 (SAS similarity theorem). Considder ∆XYZ and ∆X'Y'Z'. If ∠Z ≅ ∠Z' and XZ/X'Z' = YZ/Y'Z', then ∆XYZ ~ ∆X'Y'Z'.

Thm 6 (SAS similarity theorem). Consider ∆XYZ and ∆X'Y'Z'. If XY/X'Y' = YZ/Y'Z' = ZX/Z'X', then ∆XYZ ~ ∆X'Y'Z'.

Thm 7. Let ∆XYZ ~ ∆X'Y'Z' with ratio r. Then a∆XYZ / a∆X'Y'Z' = r^2. 

Thm 8 In XYZ, let ∠Z be a right angle and W be the foot of the perpendicular to XY through Z. Then X-W-Y, W != X, Y, and ∆XYZ ~ ∆XZW ~ ∆ZYW.
```

### 3.10 Polyhedral volume

concepts

```
Tetrahedra, their faces and interiors; regular tetrahedra
Tetrahedral regions
Congruent and similar tetrahedra
Prisms, pyramids, their bases and altitudes; right and oblique prims
Lateral edges and faces
Parallelepipedes, boxes, and cubes
Polyhedral regions
Polyhedral regions associated with prisms and pyramids
Volume axioms
Cavalieri's axiom is required
Volumes of prisms, parallelepipeds, and pyramids
```


Theorems

```
Thm 1.The intersection of the interiors of either pair of opposite dihedral angles of a tetrahedron is the same.

Thm 2.These point sets associated with tetrahedron T all coincide
    1.the set of all points between any two points on faces of T,
    2.the union of the interior and faces of T,
    3.the intersection of all convex sets that contain the vertices of T.

Thm 3. If Π is triangular, then Σ' and the intersection of Π with any plane δ parallel to and between the base planes are triangular regions congruent to Σ.

Thm 4. If the insertion of polyhedral regions Π and Ψ lies in the union of finitely many planes, then Π ∪ Ψ is a polyhedral region.

Thm 5. All prims are polyhedral regions. The intersection of a prism with a plane parallel to and between its base plane is a polygonal region. All these have the same area as the base.

Axiom V1. Regions determined by congruent tetrahedra have the same volumn.

Axiom V2. If the intersection of two polyhedral regions Π and Ψ lies in the union if finitely many planes, then v(Π ∪ Ψ) = vΠ + vΨ.

Axiom V3. The volume of a cube is the cube of one of its edge.

Axiom V4 (Cavalierr's axiom). Polyhedral regions Π and Ψ that lie between planes α and β have the same volume if for each plane ε equal to α or β or parallel to and between them, Π ∩ ε and ψ ∩ ε are polygonal regions with the same area.
```

![Cavalieri's Axiom]("/static/3.10.4_cavalieri_axiom.png")

```
Thm 6. Prisms with the same base area and altitude have the same volume.

Thm 7. The volume of a right square prism is its altitude tiems its base area.

Thm 8. The volume of any prism is its altitude times its base area.

Thm 9. The volume of a box is the product of its altitudes.

Thm 10. Let Π be a triangular pyramid with altitude α, ε be its base plane, δ be a plane parallel to ε between ε and apex O, and b be the distance from O to δ. then Π ∩ δ is a triangular region similar to the base with ratio b/a.

Thm 11. Every pyramid  is a ployhedral region. Let a be its altitude, be its base plane, be a plane parallel to between and the apex O, and b be the distance from O to ε. Then Π ∩ δ is a polygonal region with area (b/a)^2 time the base area.

Corollary 12. Pyramids with the same base area and altitude have the same volume.

Thm 13. The volume of a pyramid is one third of its altitude times its base area.
```

If two tetrahedra are similar with ratio r, then their base areas have ratio r^2, their volumes have ratio r^3.

### 3.11 Coordinate geometry

concepts

```
Cartesion coordinate system: origin, axes, and planes
Distance formula
Midpoint formula
Parallelogram law
Linear parametric equations for lines and planes
Linear equation for a plane
Plane coordinate geometry
```


theorems

```
Thm 1. Assignment of coordinates is a one-to-one correspondence between the set of all points and the set of all ordered triples of scalars.

Thm 2 (Distance formula). The distance between points P and Q is
        PQ = ((p1- q1)^2 + (p2 - q2)^2 + (p3 - q3)^2)^.5
        Thus (PQ)^2 = (P-Q)・(P-Q), the dot product

Thm 3 (Midpoint formula). The midpoint of segment PQ is 1/2(P+Q) =<1/2(p1 + q1), 1/2(p2 + q2), 1/2(p3 + q3)>.

Thm 4 (Parallelogram law). If the origin O and points P and Q are not collinear, then R = P + Q forms with them a parallelogram OPRQ.

Lemma 5. Let P be a point distinct from the origin O. Then a point X lies on OP if and only if X = Pt for some scalar t.

Thm 6. A point set g is line if and only if it's the graph of a system X = Pt +Q of linear parametric equations with P != O. Then g is the line through Q parallel or equal to OP, and the function X -> (OP)t is a scale for g.

Corollary 7. If P != Q, then X = P + (Q - P)t is a system of equations for the line PQ. Moreover,
    t = 0 <-> X = P  0 < t <-> X lies in PQ
    t = 1 <-> X = Q  0 <= t <= X lies in PQ.

Thm 8. A point set ε is a plane if and only if it's the graph of some system X = Pt + Qu + R of linear parametric equations with O, P, and Q noncollinear. In that case, ε is the plane through R parallel or equal to OPQ.

Corollary 9. If points P, Q, and R are noncollinear, then plane PQR has equations X = P + (Q - P)t + (R - P)u.

Thm 10. Consider points P and Q distinct from the origin O. Then OP ⊥ OQ if and only if the dot product P・Q = p1q1 + p2q2 + p3q3 = 0.

Thm 11. A point set ε is a plane if and only if it's the graph of some linear equation P・X = b with P != O.

```

### 3.12 Circles and spheres

concepts

```
Circles, and their interiors and exteriors
Equation of a circle
Intersections of lines and circles
Tangent lines and circles
Chords and diameters of circles
Spheres, and their interiors and exteriors
Equation of a sphere
Intersections of lines, planes, and spheres
Tangent lines, planes and spheres
Chords and diameters of spheres
Secant lines
```

theorems

```
Thm 1. Set up Cartesian coordinates. Let Γ be the circle in the 1,2 plane with center Z=<z1, z2> and radius r. Then a point X = <x1, x2> lies
    on Γ if           (x1 - z1)^2 + (x2 - z2)^2 = r^2,
    interior to Γ if  (x1 - z1)^2 + (x2 - z2)^2 < r^2,
    exterior to Γ if  (x1 - z1)^2 + (x2 - z2)^2 > r^2.

Thm 2. Let P and R be points on or interior to a circle Γ. Then all points Q != P, R between P and R lie in the interior of Γ. 

Corollary 3. The interior of a circle is convex.

Thm 4. the intersection of a coplanar line g and cirlce Γ is empty, a point, or exactly two points. The third case holds if and only if g contains a point interior to Γ.

Thm 5. Consider two distinct coplanar circles and with centers O and O' and radius r and r'. Exactly one of the following cases holds:
    0.  r > OO' + r';
    0'. r' > OO' + r;
    1.  r = OO' + r';
    1'. r' = OO' + r;
    2.  Each of OO', r, and r' is less than the sum of the other two and Γ Γ' consists of two distinct points X and Y;
    3.  OO' = r + r';
    4.  OO' > r + r';

Thm 6. Let PQ be a chord of a circle Γ with radius r. Then PQ <= 2r, and PQ = 2r if and only if PQ is a diameter of Γ.

Thm 7. Let PQ and RS be chords of a circle intersecting at a point X. Then any two of the following conditions imply the third:
    1. RS is a diameter of Γ;
    2. PQ ⊥ RS;
    3. X is the midpoint of PQ.

Thm 8. Let PR and P'R' be chords of circles with centers O and O' and the same radius. Let d and d' denote the distances from O and O' to PR and P'R'. Then PR <= P'R' if and only if d >= d'.

Thm 9. Let P be a point on a circle Γ with center O in a plane ε. The perpendicular to OP through P in ε is the unique tangent Γ to through P.

Thm 10. Let Γ be a circle with center O in a plane ε, and P be a point in ε exterior to Γ. There are exactly two tangents to Γ through P. If these intersect Γ at points Y and Z, then ∆OYP and ∆OZP are congruent right triangles.

Thm 11. Set up Cartesian coordinates. Let Σ be the sphere with center Z=<z1,z2,z3>. Then a point X=<x1,x2,x3> lies
    on Σ if           (x1 - z1)^2 + (x2 - z2)^2 + (x3 - z3)^2 = r^2,
    interior to Σ if  (x1 - z1)^2 + (x2 - z2)^2 + (x3 - z3)^2 < r^2,
    exterior to Σ if  (x1 - z1)^2 + (x2 - z2)^2 + (x3 - z3)^2 = r^2.

Thm 12. The intersection of a plane ε and a sphere Σ is empty, a point, or a circle. The last case holds if and only if ε contains a point interior to Σ.

Thm 13. Let PQ be a chord of a sphere Σ, let ε be a plane, and let PQ ∩ ε be a point X. Then any two of the following conditions imply the third:
    1. ε passes through the center of Σ;
    2. PQ ⊥ ε;
    3. X is the midpoint of PQ.

Thm 14. Let δ be a plane, let Σ be a sphere, and let δ ∩ Σ be a circle Γ. Let RS be a chord of Σ, and δ ∩ RS be a point X. Then any two of the following conditions imply the third:
    1.RS is a diameter of Σ;
    2.δ ⊥ RS;
    3.X is the center of Γ.

Thm 15. Let Σ and Σ' be sphere with centers O and O' and the same radius. Let δ and δ' be planes whose intersections with Σ and Σ' are circles with radii r and r'. Let d and d' be the distances from O and O' to δ and δ'. Then r <= r' if and only if d >= d'.

Thm 16. Let P be a point on a sphare Σ with center O. The plane ε perpendicular to OP through P is the unique plane tangent to Σ through P. A line through P is tangent to Σ if and only if it lies in ε.

Thm 17. Let X and Y be points on a sphere Σ and P be a point not on Σ. If PX and PY are tangent to Σ, then PX = PY.

```


### 3.13 Arcs and trigonometric functions

concepts

```
Angular scales and angle parameters
Major and minor arcs, semicircles, and their measures
Inscribed angles and subtended arcs
Cosines and sines
Periodic functions
Parametric equations for circles and spheres
Basic identities
Even and odd functions
Tangents
Right triangle trigonometry
```

angle measurement

```
θ = 360q + r

q is an integer, θ // 360 = q;
-180 < r <= 180, θ % 360 = r.

angular scale: a functon p from the set of all real numbers onto the set of rays in a plane ε originating at a point O, is called an angular scale at O in ε if p(α) = OA and p(β) = OB imply
    |(α - β) mod 360°| = m∠AOB.

Thm 1. Let p be an angular scale at a point O, in some plane ε. Its initial ray OZ = p(0°) and the ray OZ' = p(180°) are opposite. Let OU = p(1°). For any number α, with α* = α mod 360° and OA = p(α),
    α* = 180°       => ΟΑ = ΟΖ';
    0° < α* < 180°  => A lies on the same side of OZ in ε as U, and mZOA = α*;
    α* = 0°         => ΟΑ = ΟΖ;
    -180° < α* < 0° => A lies on the side of OZ in ε opposite U and mZOA = -α*.

Thm 2. This function p is in fact an angular scale at O in ε.

Thm 3. Let ζ be any constant. If p is an angular scale at point O in plane ε, then so are the function θ -> p(ζ + θ) and θ -> (ζ - θ). Moreover, if p' is also an angular scale at O and p(ζ) = p'(0°), then p'(θ) = p(ζ + θ) for all , or else p'(θ) = p(ζ - θ) for all θ.
    |(α - β) mod 360°| = |((ζ ± α) - (ζ ± β)) mod 360°|.

```


arcs

```
Thm 4. Let PQR and P'Q'R' be minor arcs of circles with centers O and O' and the same radius. Let d and d' denotes the distances from O and O' to PR and P'R'. Then these conditions are equivalent: m∠POR <= m∠P'O'R', mPQR <= mP'O'R' and d >= d'.

Thm 5(arc addtion theorem). Let P, Q, R, S, and T be pooints on a circle, such that PQR ∩ RST is the point R. Then PQR ∪ RST = PRT and mPQR + mRST = mPRT.

Thm 6. The measure of an inscribed angle is half that of its subtended arc.

Corollary 7. All angles inscribed in the same arc are congruent.

Corollary 8. An angle inscribed in a semicircle is a right angle. 

Corollary 9. m∠PQR = 1/2 mPSQ.

```


trigonometric functions

```
Corollary 11. Thm 10 also holds for the circle with center Z = <z1, z2> and radius r, and the mapping θ -> T = <t1, t2>, where
    t1 = z1 + rcosθ
    t2 = z2 + rsinθ


Corollary 12. The function <θ, φ> -> Τ = <t1, t2, t3>, where
    t1 = z1 + rcosθ
    t2 = z2 + rsinθ
    t3 = z3 + rcosθ,
maps the set {<θ, φ>: 0° <= θ < 360° & 0° <= φ <= 180} onto the sphere with center Z=<z1, z2, z3> and radius r.

Thm 13. For all theta, the sine and cosine satisfy the cofunction, half-turn, and supplementary-angle identities
    cosθ = sin(90° - θ)        sinθ = cos(90° - θ)
    cos(θ + 180°) = -cosθ      sin(θ + 180°) = -sinθ
    cos(180° - θ) = -conθ      sin(180° - θ) = sinθ.
moreover, even-odd
    cos(-θ) = consθ     sin(-θ) = -sinθ.

Thm 14. The tangent is an even function. For n = 0, ±1, ±2, ... and any θ, the following periodic identity holds, or else both sides are undefined: tan(θ + 180°) = tanθ.

Thm 15. In any right triangle ABC with hypotenuse c and legs a and b opposite acute angles at vertices A and B,
    cos m∠A = b/c,    a^2 + b^2 = c^2
    sin m∠B = a/c,    m∠A + m∠B = 90°
    tan m∠B = b/a.

Thm 16. Consider figure 3.13.5, where PXQ is an arc of a unit circle with center O, theta=m∠POQ, and 0° < θ < 90°, Then sinθ = QR < PQ < PS = tanθ and OS = 1/cosθ

```

![complementary vs supplementary]('./static/Complementary-and-Supplementary-Angles.jpg')


### 3.14 π

concepts

```
Polygons inscribed in arcs; regular polygons
Arc length and circumference
Proportionality of arc length to radius and to arc measure in degree π
Archimedes' approximation π
Transcendence of π
Radian measure
Definition and area of a disk and a sector
Definition and volume of a cylinder, a cone, and a ball
```

theorems

```
Thm 1. The lengths of ars of equal measure in circles with radii r and r' have the ratio r/r'.

Thm 2. Arcs of equal measure in circles of equal radius have the same length.

Lemma 3 (Length addtion). Suppose circular arc PRT is the union of arc PQR and RST. Then l(PRT) = l(PQR) + l(RST).

Lemma 4 (neq). If PQR and P'Q'R' are arcs in the same circle and mPQR < mP'Q'R', then l(PQR) < l(P'Q'R').

Thm 5. The lengths of arcs in a circle Γ have the same ratio as their degree measures.

Thm 6. The circumference of a circle Γ with radius r is 2πr. the length of a d° arc is Γ is (π / 180)d°r.
```


### 5.1 Four concurrence theorems

concepts

```
Standard triangle terminology and notation
Edge bisectors of ∆ABC
Circumcircle, circumcenter O, and Circumradius R
Angle bisectors
Incircle, incenter I, and inradius r
Medians and centroid G
Altitudes and orthocenter H
```

theorems

```
Thm 1 (Edge bisector theorem). The perpendicular bisectors of the edges of ∆ABC meet at a point O equidistant from its vertices.

Thm 2. Any three noncollinear points lie on a unique circle.

Thm 3 (angle bisector theorem). The angle bisectors of ∆ABC meet at an interior point I equidistant from the edge lines.

Thm 5 (medians theorem). The medians of ∆ABC meet at a point G two thirds of the way from any vertex to the midpoint of the opposite side.

Thm 6. The edges of the medial triangle are parallel to those of ∆ABC and half their length.

Corollary 7 (Altitudes theorem). The altitude lines of triangle ∆ABC meet at a point H.

Corollary 8. The circumcenter of a triangle is the orthocenter of its medial triangle.

```

*Concurrent* : a set of lines that pass through a single point is called concurrent. 

### 5.2 Menelaus' theorem (P.162)

concepts

```
Directed distances
Menelaus' product
Menelaus' theorem
```

### 5.3 Desargues' theorem

concepts

```
Pencils of lines
Euclidean forms of Desargues' theorem
Does Desargues' theorem require metric notions?
```

### 5.4 Ceva's theorem

concepts

```
Ceva's theorem
Derving the medians, altitudes, and angle bisectors theorems
Proving Ceva's theorem by mechanics
```


### 5.5 Trigonometry

concepts

```
Law of sines
Law of cosines
Determining other parts of a triangle from ASA, SAS, or SSS data
Using SSA data
Cosine and sine sum and difference formulas
Cosine and sine double angle formulas
SAS and ASA area formulas; Hero's SSS area formula
Area formulas involving the circumradius
Inequalities for approximating sine values
```

```
1. Law of sines
Thm 1 (Law of sines). If R is the circumradius of triangle ∆ABC, then
a / sin m∠A = b / sin m∠B = c / sin m∠C = 2R.

2. Law of cosines
Thm 2 (Law of cosines). In ∆ABC, a^2 = b^2 + c^2 - 2bccos m∠A.

Addition, subtraction, double and half angle formulas
sin(a ± b) = sin a cos b ± cos a sin b
cos(a ± b) = cos a cos b ∓ sin a sin b
sin 2a = 2sin a cos a
cos 2a = cos^2 a - sin^2 b = 2cos^2 a - 1 = 1 - 2sin^2 a

Area formulas
Thm 8(SAS and ASA area formula). The area of ∆ABC is
    a∆ABC = 1/2 bc sin m∠A = (c^2 sin m∠A sin m∠B) / (2 sin m∠C)

Thm 12. If 0° < θ < 90°, then sinθ < πθ/180° < tanθ. 

```


### 5.6 Vector product (P192 / 507)

concepts

```
Dot product
Cross Product
Distinguishing sides of lines and planes
Determinant criteria for collinearity and coplanarity
Determinant formulas for triangle area, and volume of a tetrahedron
When do four planes, or three lines in a plane, have a common point?
```

dot products

you can use the law of consines with a coordinate system and vector algebra to measure angles. Regard points P=<p1, p2, p3> and Q=<q1,q2,q3> as vectors, with dot product P・Q = p1q1 + p2q2 + p3q3.

```
Thm 1. If points P and Q are noncollinear with the origin O, then P・Q = (OP)(OQ)cos m∠POQ.

Corollary 2(angle formula). If P, X, and V are noncollinear points, then
    cos m∠PVX = (P - V)・(X - V) / (VP)(VX)

Thm 3. A point X lies on a line g = VP just in case
    det[P - V, X - V] = 0.

```


