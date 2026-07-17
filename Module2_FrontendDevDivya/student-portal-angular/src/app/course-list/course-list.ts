import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CourseCard } from '../course-card/course-card';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, CourseCard],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseList {
  courses = [
    { name: 'Angular Basics', desc: 'Learn Angular' },
    { name: 'React Basics', desc: 'Learn React' },
    { name: 'Node Basics', desc: 'Learn Node' }
  ];
}