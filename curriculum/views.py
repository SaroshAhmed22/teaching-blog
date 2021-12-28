from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from .models import Standard, Subject, Lesson, course_lesson, Comment, WorkingDays, TimeSlots
from casting.models import  Department,Semester, teacher, student , section , sec_course ,  Slots, Days, course, room, timetable, freetimetable
from django.urls import reverse_lazy
from .forms import CommentForm,ReplyForm, LessonForm
from django.http import HttpResponseRedirect
# from casting import casting

def sec_list_def(request, slug):  

    secob = section.objects.filter(dept__slug__contains=slug)
    cont = { 'section': secob}
    return render (request, 'curriculum/sec_list.html' , cont)

def sec_cou_list_def(request, slugid, slug):  
    
    slug = slug
    secob = sec_course.objects.filter(secid__id=slugid)
    cont = { 'section': secob}
    return render (request, 'curriculum/sec_cou_list.html' , cont)


class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    # model = section
    template_name = 'curriculum/standard_list_view.html'

class courseListView(ListView):
    context_object_name = 'courses'
    model = course
    # model = section
    template_name = 'curriculum/course_list_view.html'

class SubjectListView(DetailView):
    context_object_name = 'standards'
    extra_context = {
        'slots': TimeSlots.objects.all()
    }
    model = Standard
    
    template_name = 'curriculum/subject_list_view.html'

# class LessonListView(DetailView):
#     context_object_name = 'subjects'
#     model = Subject
#     # model = course
#     template_name = 'curriculum/lesson_list_view.html'

class LessonListView(DetailView):

    context_object_name = 'subjects'
    model = course
    # model = course
    template_name = 'curriculum/cou_lesson.html'

class LessonDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(request=self.request)
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name=='form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)

#  lesson2_detai

class Lesson2DetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = course_lesson
    template_name = 'curriculum/lesson2_detail.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(Lesson2DetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(request=self.request)
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name=='form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)
#  end of lesson2_detail


    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_detail',kwargs={'standard':standard.slug,
                                                             'subject':subject.slug,
                                                             'slug':self.object.slug})
    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonCreateView(CreateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = LessonForm
    context_object_name = 'subject'
    model= Subject
    template_name = 'curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})


    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(UpdateView):
    fields = ('name','position','video','ppt','Notes')
    model= Lesson
    template_name = 'curriculum/lesson_update.html'
    context_object_name = 'lessons'

class LessonDeleteView(DeleteView):
    model= Lesson
    context_object_name = 'lessons'
    template_name = 'curriculum/lesson_delete.html'

    def get_success_url(self):
        print(self.object)
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':subject.slug})
